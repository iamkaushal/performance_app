from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from login import LoginWindow
from dashboard import DashboardWindow
from kivy.core.window import Window
from fileprocessor import FileProcessor
Window.size = (1500, 700)
class PerformanceMonitorApp(App):
    username = StringProperty(None)
    password = StringProperty(None)
    def build(self):
        f = FileProcessor()
        manager = ScreenManager()
        manager.add_widget(LoginWindow(name="Login"))
        manager.add_widget(DashboardWindow(name="Dashboard"))
        f.processFiles()
        return manager

if __name__ == '__main__':
    PerformanceMonitorApp().run()