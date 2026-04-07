from kivy.app import App
from kivy.uix.widget import Widget

class HelloWorld(Widget):
    pass

class TutorCompanion(App):
    def build(self):
        return HelloWorld()