from pathlib import Path

import kivy
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

# needed for using "include" in kv files
kivy.resources.resource_add_path(str(Path(__file__).parent)) 


class PaceMonitorView(MDScreen):
    
    controller = ObjectProperty # <controller.PaceMonitorController object>.
    model = ObjectProperty # <model.PaceMonitorModel object>.

    def __init__(self, controller, model, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
    
    def on_navigation_item(self, item):
        self.controller.navigate(item)


build_file = Path(__file__).with_suffix('.kv')
Builder.load_file(str(build_file))
