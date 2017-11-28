from kivy.uix.behaviors import ToggleButtonBehavior , ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.lang import Builder

Builder.load_file('controlbar.kv')

class VideoPlayPause(ToggleButtonBehavior,Image):
    pass

class VideoStop(ButtonBehavior,Image):
    
    def stop(self,video,play_pause):
        play_pause.state='normal'
        video.state='stop'

class VideoSlider(Slider):

    def on_touch_down(self,touch):
        video=self.parent.parent.video
        if self.collide_point(*touch.pos):
            self.pre_state=video.state
            self.pre_touch=touch
            video.state='pause'
        return super().on_touch_down(touch)

    def on_touch_up(self,touch):
        if self.collide_point(*touch.pos) and hasattr(self,'pre_touch') and touch is self.pre_touch:
            video=self.parent.parent.video
            video.seek(self.value)
            if self.pre_state != 'stop':
                video.state=self.pre_state
        return super().on_touch_up(touch)