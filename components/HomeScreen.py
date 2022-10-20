from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.screen import MDScreen
import certifi, json

from components.ArticleRV import ArticleRV

from api import API_KEY

class HomeScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        #Clock.schedule_once(self.set_toolbar_font)
        # Clock.schedule_once(self.get_news)
        
        
    def set_toolbar_font(self, *args):
        self.ids.toolbar.ids.label_title.color = "#000000"
        self.ids.toolbar.ids.label_title.font_style = "Body1"
        self.ids.toolbar.ids.label_title.font_name = "Poppins"
    
    def get_json_news(self):
        with open("results.json", "r", encoding='utf-8') as file:
            data = json.load(file)
        an_article = data['articles'][0]
    
    def get_news(self, *args):
        url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={API_KEY}"
        headers = {'User-Agent': 'My Agent'}
        self.request = UrlRequest(url, self.res, ca_file=certifi.where(), verify=True, req_headers=headers)
    
    # Save to avoid calling api multiple times
    def save_json_test(self):
    	with open("results.json", "w",encoding='utf-8') as file:
            json.dump(self.request.result, file, ensure_ascii=False, indent=4)

    def res(self,*args):
        print("Result: after success", self.request.result)
        self.save_json_test()