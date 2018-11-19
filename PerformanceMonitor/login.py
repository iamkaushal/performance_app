from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
import MySQLdb

db = MySQLdb.connect(host="localhost",user="root", passwd="",db="dbtester")
Builder.load_file('login.kv')
class LoginWindow(Screen):
    def login(self,usernameText,passwordText):
        app = App.get_running_app()
        app.username = usernameText
        app.password = passwordText
        authenticationResult = self.authenticate(usernameText,passwordText)
        if authenticationResult == "True":
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = "Dashboard"
        else:
            print(authenticationResult)
        
    def build(self):
        pass

    def authenticate(self,username,password):
        cursor = db.cursor()
        cursor.execute("select username from users where username = %s",[username])
        dbuser = cursor.fetchone()[0]
        if dbuser == username:
            cursor.execute("select password from users where username = %s",[username])
            dbpass = cursor.fetchone()[0]
            if dbpass == password:
                return "True"
            else:
                return "Password Incorrect"
        else:
            return "Username Incorrect."