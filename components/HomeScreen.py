from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest

from kivymd.uix.screen import MDScreen

class HomeScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.set_toolbar_font)
        Clock.schedule_once(self.get_news)
        
    def set_toolbar_font(self, *args):
        self.ids.toolbar.ids.label_title.color = "#000000"
        self.ids.toolbar.ids.label_title.font_style = "Body1"
        self.ids.toolbar.ids.label_title.font_name = "Poppins"
    
    def on_start(self, **kwargs):
    	print("hi")
    
    def get_news(self, *args):   
        url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=7c97ff4614c24b11a0f272c78e511a36"
        print(url)
        self.req = UrlRequest(url, self.res)
        
    def res(self, *args):
        print("yes")
        print(self.req.result)
        self.ids.label.text = self.req.result