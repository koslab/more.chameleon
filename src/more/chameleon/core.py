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
    
    def __init__(self, path):
        self.repository = PageTemplateLoader(path)

    def __call__(self, name):
        return Renderer(name, self.repository)

class Renderer(object):

    def __init__(self, name, repository):
        self.name = name
        self.repository = repository

    def static_url(self, component):
        return request.app.bower_components.get_component(
            component).url()

    def template_globals(self, request):
        settings = request.app.registry.settings.chameleon
        result = {
            'application_url': request.application_url,
            'request': request,
            'templates': self.repository,
            'static_url': self.static_url
        }
        return result

    def __call__(self, content, request):
        settings = request.app.registry.settings.chameleon
        template = self.repository[self.name]
        template.auto_reload = settings.auto_reload

        result = template(
                options=content, **self.template_globals(request)
        )

        return Response(result, content_type='text/html')
