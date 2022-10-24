import os
from config import KV_DIR, FONT_DIR
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'height', '853')
Config.set('graphics', 'width', '480')
Config.set('kivy', 'default_font', 
    ["Poppins", 
        os.path.join(FONT_DIR,"Poppins-Regular.ttf"), 
        os.path.join(FONT_DIR,"Poppins-Italic.ttf"),
        os.path.join(FONT_DIR,"Poppins-Bold.ttf"), 
        os.path.join(FONT_DIR,"Poppins-BoldItalic.ttf")
    ]
)

from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles

from components.HomeScreen import HomeScreen
        
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