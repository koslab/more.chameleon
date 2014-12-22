# The MIT License (MIT)
# 
# Copyright (c) 2014 Mohd Izhar Firdaus Ismail
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# 

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

class StaticUrl(object):

    def __init__(self, request):
        self.components = request.app.bower_components

    def __call__(self, component):
        return self.components.get_component(component).url()
        
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
            'static_url': StaticUrl(request)
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
