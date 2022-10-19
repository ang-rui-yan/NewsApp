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
from kivymd.font_definitions import theme_font_styles


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView



Builder.load_string('''
<RV>:
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]


class TestApp(App):
    def build(self):
        self.register_font()
        return RV()
    def register_font(self):
        LabelBase.register(
            name="Poppins",
            fn_regular=os.path.join(FONT_DIR,"Poppins-Regular.ttf"))

if __name__ == '__main__':
    TestApp().run()