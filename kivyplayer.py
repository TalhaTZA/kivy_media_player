from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.actionbar import ActionPrevious
from kivy.lang import Builder
from kivy.uix.popup import Popup
from videocontroller import VideoController
from loaddialog import LoadDialog

Builder.load_file('actiontextinput.kv')

class ActionListButton(ToggleButtonBehavior,ActionPrevious):
    pass


class KivyPlayer(FloatLayout):
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
        pass
    
    def dismiss_popup(self):
        self.popup.dismiss()

    
    def search(self,text):
        pass

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