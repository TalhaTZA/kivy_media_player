from kivy.uix.video import Video as KivyVideo
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import NumericProperty ,  ObjectProperty , StringProperty
from subtitles import Subtitles

Builder.load_file('subtitle.kv')
Builder.load_file('video.kv')



class Video(KivyVideo):
    image=ObjectProperty(None)
    surl=StringProperty(None)

    def on_state(self,instance,value):
        if self.state== 'play':
            self.cover.opacity=0
            self.color=(1,1,1,1)

        elif self.state == 'stop':
            self.seek(0)
            self.color=(0,0,0,0)
            self.cover.opacity=1
        return super().on_state(instance,value)

    def on_eos(self,instance,value):
        if value:
            self.state='stop'
    
    def _on_load(self,*largs):
        super()._on_load(largs)
        self.color=(1,1,1,1)
    
    def on_source(self,instance,value):
        self.color=(0,0,0,0)
        self.subs=Subtitles(self.surl)
        self.sub=None
    
    def on_position(self,instance,value):
        #print(self.subs.subtitles)
        next_sub=self.subs.next(value)
        if next_sub is None:
            self.clear_subtitle()
        else:
            sub=self.sub
            st='startTime'
            if sub is None or sub[st] != next_sub[st]:
                self.display_subtitle(next_sub)
    
    def clear_subtitle(self):
        if self.slabel.text != "":
            self.sub = None
            self.slabel.text = ""
            self.slabel.bcolor = (0.1, 0.1, 0.1, 0)
    
    def display_subtitle(self, sub):
        self.sub = sub
        self.slabel.text = sub['content']
        print(self.slabel.text)
        self.slabel.bcolor = (0.1, 0.1, 0.1, .8)
    
    def on_image(self,instance,value):
        self.cover.opacity=1

Factory.unregister('Video')
Factory.register('Video',cls=Video)