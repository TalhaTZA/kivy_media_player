from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.actionbar import ActionPrevious
from kivy.lang import Builder
from kivy.uix.popup import Popup
from videocontroller import VideoController
from loaddialog import LoadDialog
import json, os
from sidebar import ListItem
from kivy.network.urlrequest import UrlRequest

Builder.load_file('actiontextinput.kv')

_surl = 'https://www.ted.com/talks/subtitles/id/%s/lang/en'
_meta = 'https://api.ted.com/v1/talks/%s.json?api-key=%s'
_api = '79bcca13c0cc74523125332a1032ff104b62a163'
_search = 'https://api.ted.com/v1/search.json?q=%s&categories=talks&api-key=%s'

class ActionListButton(ToggleButtonBehavior,ActionPrevious):
    def on_state(self,instance,value):
        if value== 'normal':
            self.animationSB=Animation(right=0)
            self.animationSB.start(self.root.side_bar)
        else:
            self.root.side_bar.x=0


class KivyPlayer(FloatLayout):
    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.playlist.bind(minimum_height=self.playlist.setter('height'))

    def hide_bars(self,instance,playing):
        if playing:
            self.list_button.state='normal'
            self.animationAB=Animation(y=self.height)
            self.action_bar.disabled=True
            self.animationAB.start(self.action_bar)
        else:
            self.action_bar.disabled=False
            self.action_bar.top=self.height
            if hasattr(self,'animationAB'):
                self.animationAB.cancel(self.action_bar)
    
    def toogle_mute(self,instane,state):
        if state== 'down':
            self.video_controller.video.volume=0
        else:
            self.video_controller.video.volume=1
    
    def show_load_list(self):
        content=LoadDialog(load=self.load_list,cancel=self.dismiss_popup)
        self.popup=Popup(title='Load a file first',content=content,size_hint=(1,1))
        self.popup.open()
    
    def load_list(self,path,filename):
        json_data=open(os.path.join(path, filename[0]))
        #print(path)
        data = json.load(json_data)
        json_data.close()
        self.load_from_json(data,0)
    
    def dismiss_popup(self):
        self.popup.dismiss()

    def load_from_json(self,data,flag=1):
        self.playlist.clear_widgets()
        for val in data['results']:
            t = val['talk']
            video = self.video_controller.video
            if flag==0:
                meta= ('results/{}.json').format(t['id'])
            else:
                meta = _meta % (t['id'],_api)
            surl = _surl % t['id']
            item = ListItem(video, meta, surl,text=t['name'])
            self.playlist.add_widget(item)
        self.dismiss_popup()
        self.list_button.state = 'down'

    def search(self,text):
        url=_search %(text,_api)
        #print(url)
        req=UrlRequest(url,on_success=self.got_search)
    
    def got_search(self,req,result):
        self.load_from_json(result)

class KivyPlayerApp(App):
    def build(self):
        return KivyPlayer()
        '''self.video=Video()
        self.video.bind(on_touch_down=self.touch_down)
        return self.video

    def touch_down(self,instance,touch):
        if self.video.state== 'play':
            self.video.state='pause'
        else:
            self.video.state='play'
        
        if touch.is_double_tap:
            self.video.state='stop'''

if __name__ in ('__main__'):
    KivyPlayerApp().run()