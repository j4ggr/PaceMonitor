from view.view import PaceMonitorView, build_view_content


class PaceMonitorController():
    """
    Coordinates work of the view with the model.

    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """
    def __init__(self, model):
        """
        The constructor takes a reference to the model.
        The constructor creates the view.
        """
        self.model = model
        self.view = PaceMonitorView(controller=self, model=self.model)

    def get_screen(self):
        build_view_content()
        return self.view

    def navigate(self, navigation_item):
        screen_name = f'{navigation_item.name}_screen'
        self.view.navigation_screens.current = screen_name
