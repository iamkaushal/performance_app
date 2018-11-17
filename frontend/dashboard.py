from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

Builder.load_file('dashboard.kv')
class DashboardWindow(Screen):
    Window.size = (1200, 650)
    def build(self):
        pass