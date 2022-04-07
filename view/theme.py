import darkdetect

from kivy.core.text import LabelBase

from kivymd import fonts_path
from kivymd.theming import ThemeManager


colors = {
    'LightBlue': {
        '50': 'F2FAFF',
        '100': 'CCEEFF',
        '200': '97DAFC',
        '300': '60C1F2',
        '400': '2EAAE8',
        '500': '0091DC',
        '600': '0081C1',
        '700': '0070A8',
        '800': '005D8C',
        '900': '004A70',
        'A100': 'CCEEFF',
        'A200': '97DAFC',
        'A400': '2EAAE8',
        'A700': '0070A8'},

    'BlueGray': {
        '50': 'F7F8F9',
        '100': 'EAECEF',
        '200': 'DEE1E5',
        '300': 'D2D6DB',
        '400': 'C4CAD1',
        '500': 'B6BEC6',
        '600': '99A2AA',
        '700': '7F878E',
        '800': '646C72',
        '900': '4A5156',
        'A100': 'EAECEF',
        'A200': 'DEE1E5',
        'A400': 'C4CAD1',
        'A700': '7F878E'},
    
    'Red': { # Red must be included
        '50': 'FFEBEE',
        '100': 'FFCDD2',
        '200': 'EF9A9A',
        '300': 'E57373',
        '400': 'EF5350',
        '500': 'F44336',
        '600': 'E53935',
        '700': 'D32F2F',
        '800': 'C62828',
        '900': 'B71C1C',
        'A100': 'FF8A80',
        'A200': 'FF5252',
        'A400': 'FF1744',
        'A700': 'D50000'},

    'Light': {
        'StatusBar': 'E0E0E0',
        'AppBar': 'F5F5F5',
        'Background': 'FF6A00',
        'CardsDialogs': 'FFFFFF',
        'FlatButtonDown': 'cccccc'},

    'Dark': {
        'StatusBar': '22252A',
        'AppBar': '22252A',
        'Background': '282C34',
        'CardsDialogs': '404753',
        'FlatButtonDown': '999999'}}

fonts = [
    {
        'name': 'Roboto',
        'fn_regular': fonts_path + 'Roboto-Regular.ttf',
        'fn_bold': fonts_path + 'Roboto-Bold.ttf',
        'fn_italic': fonts_path + 'Roboto-Italic.ttf',
        'fn_bolditalic': fonts_path + 'Roboto-BoldItalic.ttf'},
    {
        'name': 'RobotoThin',
        'fn_regular': fonts_path + 'Roboto-Thin.ttf',
        'fn_italic': fonts_path + 'Roboto-ThinItalic.ttf'},
    {
        'name': 'RobotoLight',
        'fn_regular': fonts_path + 'Roboto-Light.ttf',
        'fn_italic': fonts_path + 'Roboto-LightItalic.ttf'},
    {
        'name': 'RobotoMedium',
        'fn_regular': fonts_path + 'Roboto-Medium.ttf',
        'fn_italic': fonts_path + 'Roboto-MediumItalic.ttf'},
    {
        'name': 'RobotoBlack',
        'fn_regular': fonts_path + 'Roboto-Black.ttf',
        'fn_italic': fonts_path + 'Roboto-BlackItalic.ttf'},
    {
        'name': 'Icons',
        'fn_regular': fonts_path + 'materialdesignicons-webfont.ttf'}]

for font in fonts:
    LabelBase.register(**font)

# font name, size (sp), always caps, letter spacing (sp)
font_styles = {
    'H1': ['RobotoLight', 96, False, -1.5],
    'H2': ['RobotoLight', 60, False, -0.5],
    'H3': ['Roboto', 48, False, 0],
    'H4': ['Roboto', 34, False, 0.25],
    'H5': ['Roboto', 24, False, 0],
    'H6': ['RobotoMedium', 20, False, 0.15],
    'Subtitle1': ['Roboto', 16, False, 0.15],
    'Subtitle2': ['RobotoMedium', 14, False, 0.1],
    'Body1': ['Roboto', 16, False, 0.5],
    'Body2': ['Roboto', 14, False, 0.25],
    'Button': ['RobotoMedium', 14, True, 1.25],
    'Caption': ['Roboto', 10, False, 0.4],
    'Overline': ['Roboto', 10, True, 1.5],
    'Icon': ['Icons', 32, False, 0]}


class Theme(ThemeManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = colors

        self.primary_palette = 'LightBlue'
        self.primary_hue = '500'
        self.primary_dark_hue = '700'
        self.primary_light_hue = '300'

        self.accent_palette = 'BlueGray'
        self.accent_hue = '500'
        self.accent_dark_hue = '700'
        self.accent_light_hue = '300'

        self.material_style = 'M3'
        self.theme_style = darkdetect.theme()
        self.font_styles = font_styles
