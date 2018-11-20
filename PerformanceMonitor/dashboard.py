from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
from kivy.lang.builder import Builder
from kivy.properties import StringProperty

Builder.load_file('dashboard.kv')

class DashboardWindow(Screen):
    def build(self):
        pass