from kivy.clock import Clock
from kivymd.uix.screen import MDScreen

from components.ArticleRV import ArticleRV, ArticleCard


class HomeScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.set_toolbar_font)
        
    def set_toolbar_font(self, *args):
        self.ids.toolbar.ids.label_title.color = "#000000"
        self.ids.toolbar.ids.label_title.font_style = "Body1"
        self.ids.toolbar.ids.label_title.font_name = "Poppins"