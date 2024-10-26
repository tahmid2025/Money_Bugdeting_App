from kivy.app import App # this helps run the application 
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.floatlayout import FloatLayout # helps with the layout


''' This class is the main starting page for the program
 it will include the logo, the login and sign in button'''
class StartPage(Screen):
    def __init__(self, **kwargs):
        super(StartPage, self).__init__(**kwargs)
        layout = FloatLayout()  # Switch to FloatLayout for custom positioning

        self.add_widget(layout)
     

class MyApp(App):
    def build(self):
        # Create a ScreenManager
        self.title = 'Tahmids budgeting App'

        sm = ScreenManager()
        

        # Add screens
        sm.add_widget(StartPage(name='start'))
        return sm


if __name__ == '__main__':
    MyApp().run()
