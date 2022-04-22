from kivy.app import App #istd3a wajiha
from kivy.lang import Builder #istd3a cod mn milf 5ariji
from kivy.core.window import Window #nthakm b5asiyt lwindaw [size , color]
from kivy.uix.screenmanager import ScreenManager , Screen
Window.clearcolor = (7/255, 122/255, 253/255, 0.02/255)
Window.size = (400,600)

class MineWindow(Screen):
    pass
class SucendWindow(Screen):
    pass

class ErrorWindow(Screen):
    pass

class Python(Screen):
    pass

class Bash(Screen):
    pass

class Php(Screen):
    pass

class Css(Screen):
    pass

class Html(Screen):
    pass

class JavaScript(Screen):
    pass

class WindowManger(ScreenManager):
    pass

kv = Builder.load_file('myapp.kv')
class Myapp(App):
    def build(self):
        self.title = "Programing"
        return kv

Myapp().run()
