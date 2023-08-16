import os
from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class AppPaths:
    APP: Path = Path(__file__).parent
    KIVY_HOME: Path = Path(__file__).parent/'.kivy'
    VIEW: Path = Path(__file__).parent/'view'
    APPNAME: str = Path(__file__).parent.name
    APPDATA: Path = Path.home()/Path(__file__).parent.name
    CONFIG: Path = Path.home()/Path(__file__).parent.name/'config'
    LOG: Path = Path.home()/Path(__file__).parent.name/'logs'
    DATA: Path = Path.home()/Path(__file__).parent.name/'data'
PATHS = AppPaths()

PATHS.APPDATA.mkdir(parents=True, exist_ok=True)
PATHS.CONFIG.mkdir(parents=True, exist_ok=True)
PATHS.LOG.mkdir(parents=True, exist_ok=True)
PATHS.DATA.mkdir(parents=True, exist_ok=True)

os.environ['KIVY_HOME'] = str(PATHS.KIVY_HOME)

@dataclass(frozen=True)
class Icon:
    BRAIN: str = 'brain'
    BRIDGE: str = 'bridge'
ICON = Icon()

from view import Theme
THEME = Theme()

import kivy
from kivy.logger import Logger
