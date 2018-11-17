from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
from kivy.lang.builder import Builder
from kivy.properties import StringProperty

Builder.load_file('login.kv')
class LoginWindow(Screen):
    def login(self,usernameText,passwordText):
        app = App.get_running_app()
        app.username = usernameText
        app.password = passwordText
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "Dashboard"
        
    def build(self):
        pass