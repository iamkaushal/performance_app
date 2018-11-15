from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string('''
LoginWindow:
    Background:
<Background>
    canvas:
        Color:
            rgb: (1,1,1)
        Rectangle:
            pos: self.pos
            size: self.size
        

''')
class LoginWindow(Widget):
    
    def build(self):
        pass

class PerformanceMonitorApp(App):
    def build(self):
        return LoginWindow()


if __name__ == '__main__':
    PerformanceMonitorApp().run()

