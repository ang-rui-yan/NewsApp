from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.screen import MDScreen
import certifi
from api import API_KEY

class HomeScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.set_toolbar_font)
        self.get_news()
        
    def set_toolbar_font(self, *args):
        self.ids.toolbar.ids.label_title.color = "#000000"
        self.ids.toolbar.ids.label_title.font_style = "Body1"
        self.ids.toolbar.ids.label_title.font_name = "Poppins"
    
    def get_news(self):
        url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={API_KEY}"
        headers = {'User-Agent': 'My Agent'}
        self.request = UrlRequest(url, self.res, ca_file=certifi.where(), verify=True, req_headers=headers)

    def res(self,*args):
        print("Result: after success", self.request.result)