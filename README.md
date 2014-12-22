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
