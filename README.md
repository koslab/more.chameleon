more.chamelon : Chameleon template support for MorePath
========================================================

This package provides chameleon renderer for morepath. 

Using the renderer
------------------------

Initialize template repository:

    from more.chameleon import Repository
    import os

    templates = Repository(
         os.path.join(os.path.directory(__file__)),'templates'),
    )

Hooking up the registry


    def main():
        config = morepath.Config()
        ....
        config.scan(more.chameleon)
        ....

Using the renderer

    @App.view(model=MyModel, render=templates('templatename.pt'))
    def myview(self, request):
        ....



Overriding settings
--------------------

You may override settings through:

    @App.setting_section(section='chameleon')
    def get_setting_section():
        return {
            'auto_reload': False, # auto reload templates
        }

Template globals
-----------------

Following are template globals passed to the template on render:

*   request - the request object
*   templates - the PageTemplateLoader repository
*   static_url - returns static url of more.static component
*   options - values returned from the view function
