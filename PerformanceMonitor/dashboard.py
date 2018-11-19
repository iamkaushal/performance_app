from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.dropdown import DropDown

Builder.load_file('dashboard.kv')
class CustomDropDown(DropDown):
    pass

class DashboardWindow(Screen):
    
    def build(self):
        
        pass