import json
import ast
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from subtitles import Subtitles

Builder.load_file('sidebar.kv')

class ListItem(ToggleButton):
    video=ObjectProperty(None)

    def __init__(self, video,meta,surl, **kwargs):
        super().__init__(**kwargs)
        self.video=video
        self.meta=meta
        self.surl=surl
    
    def on_state(self,instance,value):
        if self.state=='down':
            data=json.load(open(self.meta))['talk']
            self.video.surl=self.surl
            self.video.source="check2.mp4"
            self.video.image=data['images'][-1]['image']['url']
            req=UrlRequest(self.meta,on_success=self.got_meta)

    def got_meta(self,req,result):
        data=result['talk']
        self.video.surl=self.surl
        self.video.source=data['media']['internal']['950k']['uri']
        self.video.image=data['images'][-1]['image']['url']
    