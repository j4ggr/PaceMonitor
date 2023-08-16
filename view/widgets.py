from kivy.clock import Clock
from kivy.properties import ListProperty
from kivy.uix.dropdown import DropDown

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.behaviors import SpecificBackgroundColorBehavior


class DropdownMenuContainer(MDGridLayout, CommonElevationBehavior, ThemableBehavior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DropdownSelectable(OneLineListItem, SpecificBackgroundColorBehavior):
    def __init__(self, dropdown_caller, *args, **kwargs):
        self.dropdown_caller = dropdown_caller
        super().__init__(*args, **kwargs)

    def on_release(self):
        self.dropdown_caller.text = self.text


class DropdownTextField(MDTextField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._remove_focus_allowed = True
        self.default_text = "Select..."
        self.text = self.default_text
        self.list = DropdownMenu(self)
        self.list.entries = [f"entry {i}" for i in range(5)]
        self.is_open = False

    @property
    def bbox_icon_right(self):
        """Get bounding box coordinates of right icon as
        (left, right, bottom, top)"""
        bbox = (
            self.right - self.height,
            self.right,
            self.center_y - self.height / 2,
            self.center_y + self.height / 2,
        )
        return bbox

    @property
    def app(self):
        return MDApp.get_running_app()

    def collide_right_icon(self, touch):
        """Check if touch position is inside the right icon axis
        aligned bounding box"""
        x0, x1, y0, y1 = self.bbox_icon_right
        return x0 <= touch.x <= x1 and y0 <= touch.y <= y1

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        if not self.collide_right_icon(touch):
            return
        if self.focus and self._remove_focus_allowed:
            self.focus = False

    def on_focus(self, instance_text_field, focus: bool) -> None:
        super().on_focus(instance_text_field, focus)
        self.icon_right = self.open_close_icons[focus]
        if focus:
            if self.text == self.default_text:
                self.text = ""
            self._delay_remove_focus_()
            self.list.open(self)
        else:
            if not self.text:
                self.text = self.default_text
            self.list.dismiss()

    def _delay_remove_focus_(self):
        """Function to add a delay"""
        self._remove_focus_allowed = False

        def allow_remove_focus(*args):
            self._remove_focus_allowed = True

        Clock.schedule_once(allow_remove_focus, 0.001)

    def on_text(self, caller, text):
        if text == self.default_text: return
        view = [e for e in self.list.entries if text.lower() in e.lower()]
        self.list.view = view


class DropdownMenu(
        DropDown, ThemableBehavior, SpecificBackgroundColorBehavior, 
        CommonElevationBehavior):
    
    view = ListProperty()

    def __init__(self, caller: DropdownTextField, *args, **kwargs):
        super().__init__(*args, **kwargs)
        container = DropdownMenuContainer()
        super().add_widget(container)
        self.container = container
        self.caller = caller
        self._entries = []

    @property
    def entries(self):
        return self._entries

    @entries.setter
    def entries(self, entries: list):
        entries = list(set(entries))
        entries.sort()
        if entries == self.entries: return
        self._entries = entries
        self.view = entries
    
    def on_view(self, caller, view):
        self.clear_widgets()
        for entry in view:
            radius = [0, 0, 0, 0]
            if entry == view[0]: radius[:2] = self.radius[:2]
            if entry == view[-1]: radius[2:] = self.radius[2:]
            self.add_widget(DropdownSelectable(self.caller, text=entry, radius=radius))
    
    def on_dismiss(self):
        self.view = self.entries