from morepath.app import App
from reg import dispatch
from chameleon import PageTemplateLoader
from morepath.request import Response
from morepath.reify import reify

@App.setting_section(section='chameleon')
def get_setting_section():
    return {
        'auto_reload': False
    }

class Repository(object):
    
    def __init__(self, path, main_template=None, static_component=None):
        self.repository = PageTemplateLoader(path)
        self.main_template = main_template
        self.static_component = static_component

    def __call__(self, name):
        return Renderer(name, self.repository, self.main_template, 
                        self.static_component)

class Renderer(object):

    def __init__(self, name, repository, main_template, static_component):
        self.name = name
        self.repository = repository
        self.main_template = main_template
        self.static_component = static_component

    def template_globals(self, request):
        settings = request.app.registry.settings.chameleon
        result = {
            'application_url': request.application_url,
            'request': request
        }

        if self.main_template:
            result['main_template'] = self.repository[self.main_template]
        if self.static_component:
            result['static_url'] = request.app.bower_components.get_component(
                    self.static_component).url()
        return result

    def __call__(self, content, request):
        settings = request.app.registry.settings.chameleon
        template = self.repository[self.name]
        template.auto_reload = settings.auto_reload

        result = template(
                options=content, **self.template_globals(request)
        )

        return Response(result, content_type='text/html')
