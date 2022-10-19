import os
from config import KV_DIR, FONT_DIR
from kivy.config import Config
Config.set('kivy', 'default_font', 
    ["Poppins", 
        os.path.join(FONT_DIR,"Poppins-Regular.ttf"), 
        os.path.join(FONT_DIR,"Poppins-Italic.ttf"),
        os.path.join(FONT_DIR,"Poppins-Bold.ttf"), 
        os.path.join(FONT_DIR,"Poppins-BoldItalic.ttf")
    ]
)

from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.font_definitions import theme_font_styles
        

class HomeScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.set_toolbar_font)

    def set_toolbar_font(self, *args):
        self.ids.toolbar.ids.label_title.color = "#000000"
        self.ids.toolbar.ids.label_title.font_style = "Body1"
        self.ids.toolbar.ids.label_title.font_name = "Poppins"
        
class NewsApp(MDApp):
    def build(self):
        self.load_all_kv_files(KV_DIR)
        self.register_font()
        return HomeScreen()

    def register_font(self):
        LabelBase.register(
            name="Poppins",
            fn_regular=os.path.join(FONT_DIR,"Poppins-Regular.ttf"))
        theme_font_styles.append('Poppins')
        self.theme_cls.font_styles["Poppins"] = [
            "Poppins",
            16,
            False,
            0.15,
        ]
    
    


if __name__ == "__main__":
    NewsApp().run()