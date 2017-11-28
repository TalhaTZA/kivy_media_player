from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import ObjectProperty


import video
import controlbar

Builder.load_file('videocontroller.kv')

class VideoController(FloatLayout):
    playing=ObjectProperty(None)

    def on_playing(self,insatnce,value):
        if value:
            self.aimationVB=Animation(top=0)
            self.control_bar.disabled=True
            self.aimationVB.start(self.control_bar)
        else:
            self.play_pause.state='normal'
            self.control_bar.disabled=False
            self.control_bar.y=0
    
    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            if hasattr(self,'aimationVB'):
                self.aimationVB.cancel(self.control_bar)
            self.play_pause.state='normal'
        return super().on_touch_down(touch)