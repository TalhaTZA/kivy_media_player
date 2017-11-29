from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('loaddialog.kv')


class LoadDialog(FloatLayout):
    load=ObjectProperty(None)
    cancel=ObjectProperty(None)