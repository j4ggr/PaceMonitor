import os
from dataclasses import dataclass
from pathlib import Path

APP_DIR = Path(__file__).parent
KIVY_HOME_DIR = APP_DIR/'.kivy'
VIEW_DIR = APP_DIR/'View'

os.environ['KIVY_HOME'] = str(KIVY_HOME_DIR)

@dataclass(frozen=True)
class Icon:
    BRAIN: str = 'brain'
    BRIDGE: str = 'bridge'
ICON = Icon()

from view import Theme
THEME = Theme()

import kivy
from kivy.logger import Logger
