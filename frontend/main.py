from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen , SlideTransition
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from login import LoginWindow
from dashboard import DashboardWindow

class PerformanceMonitorApp(App):
    username = StringProperty(None)
    password = StringProperty(None)
    def build(self):
        manager = ScreenManager()
        manager.add_widget(LoginWindow(name="Login"))
        manager.add_widget(DashboardWindow(name="Dashboard"))
        return manager

if __name__ == '__main__':
    PerformanceMonitorApp().run()