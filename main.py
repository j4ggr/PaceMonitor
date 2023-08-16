import config
from kivymd.app import MDApp
from controller import PaceMonitorController
from model import PaceMonitorModel


class PaceMonitor(MDApp):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.model = PaceMonitorModel()
        self.controller = PaceMonitorController(self.model)
    
    def build(self):
        self.theme_cls = config.THEME
        return self.controller.get_screen()

if __name__ == '__main__':
    app = PaceMonitor()
    app.run()
