from morepath.app import App
from reg import dispatch
from chameleon import PageTemplateLoader
from morepath.request import Response
from morepath.reify import reify

@App.setting_section(section='chameleon')
def get_setting_section():
    return {
        'main_template': 'main_template.pt',
        'debug': False
    }

class Repository(object):
    
    def __init__(self, path, static=None):
        self.repository = PageTemplateLoader(path)
        self.static = static

    def __call__(self, name):
        return Renderer(name, self.repository, self.static)

class Renderer(object):

    def __init__(self, name, repository, static_component):
        self.name = name
        self.repository = repository
        self.static_component = static_component

    def template_globals(self, request):
        settings = request.app.registry.settings.chameleon
        result = {
            'main_template': self.repository[settings.main_template],
            'application_url': request.application_url
        }

        if self.static_component:
            result['static_url'] = request.app.bower_components.get_component(
                    self.static_component).url()
        return result

    def __call__(self, content, request):
        settings = request.app.registry.settings.chameleon
        template = self.repository[self.name]
        if settings.debug:
            template.auto_reload = True

        result = template(
                options=content, **self.template_globals(request)
        )

        return Response(result, content_type='text/html')
