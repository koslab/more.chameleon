import morepath.app import App
from reg import dispatch
from chameleon import PageTemplateLoader
from morepath.request import Response
from morepath.reify import reify

@App.setting_section(section='chameleon')
def get_setting_section():
    return {
        'main_template': 'main_template.pt',
        'use_bowerstatic': True,
        'static_component': 'static',
        'debug': False
    }

class Repository(object):
    
    def __init__(self, path):
        self.repository = PageTemplateLoader(path)

    def __call__(self, name):
        return Renderer(name)

class Renderer(object):

    def __init__(self, name, repository)
        self.name = name
        self.repository = repository

    def template_globals(self, request):
        settings = request.app.registry.settings.chameleon
        result = {
            'main_template': self.repository[settings.main_template],
            'application_url': request.application_url
        }

        if settings.use_bowerstatic:
            result['static_url'] = request.app.bower_components.get_component(
                    settings.static_component).url()
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
