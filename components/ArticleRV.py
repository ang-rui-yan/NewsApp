from datetime import datetime
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest

from kivy.properties import BooleanProperty, StringProperty
from kivymd.uix.card import MDCard

from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivymd.uix.recycleview import MDRecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout

from api import API_KEY
import certifi, json


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class ArticleCard(RecycleDataViewBehavior, MDCard):
    ''' Add selection support to the Label '''
    index = None
    article_title = StringProperty()
    article_source = StringProperty()
    article_published_at = StringProperty()
    
    url = StringProperty()
    urlToImage = StringProperty()
    
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    
    def __init__(self, **kwargs):
        super(ArticleCard, self).__init__(**kwargs)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        self.article_title = (data["title"][:90] + '...') if len(data["title"]) > 92 else data["title"]
        self.article_source = str(data["source"]["name"])
        time = datetime.fromisoformat(data["publishedAt"][:-1] + '+00:00')
        self.article_published_at = time.strftime("%d/%m/%Y, %H:%M")
        super(ArticleCard, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(ArticleCard, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]["title"]))
        else:
            print("selection removed for {0}".format(rv.data[index]["title"]))

    def on_release(self, *args):
        import webbrowser
        webbrowser.open(self.url)
        print("go to another page")

class ArticleRV(MDRecycleView):
    def __init__(self, **kwargs):
        super(ArticleRV, self).__init__(**kwargs)
        Clock.schedule_once(self.get_json_news)
        # Clock.schedule_once(self.get_news)
        
    def get_json_news(self, *args):
        with open("results.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            self.data = data["articles"]
        
        if not self.data:
            self.data = [{'text': 'Error: Please refresh'}]
        
    # Save to avoid calling api multiple times
    def save_json_test(self):
    	with open("results.json", "w",encoding='utf-8') as file:
            json.dump(self.request.result, file, ensure_ascii=False, indent=4)
    
    def get_news(self, *args):
        url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={API_KEY}"
        headers = {'User-Agent': 'My Agent'}
        self.request = UrlRequest(url, self.res, ca_file=certifi.where(), verify=True, req_headers=headers)
    

    def res(self,*args):
        print("Result: after success", self.request.result)
        self.save_json_test()