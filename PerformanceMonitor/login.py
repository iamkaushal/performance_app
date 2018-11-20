from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from database import DatabaseManagement

Builder.load_file('login.kv')
class LoginWindow(Screen):
    def login(self,usernameText,passwordText):
        db = DatabaseManagement()
        app = App.get_running_app()
        app.username = usernameText
        app.password = passwordText
        authenticationResult = db.authenticate(usernameText,passwordText)
        if authenticationResult == "True":
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = "Dashboard"
        else:
            print(authenticationResult)
        
    def build(self):
        pass