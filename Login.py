from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput  
from kivy.uix.button import Button

'''THIS CLASS IS CREATED TO ALLOW EXISTING USERS TO LOG INTO THEIR ACCOUNTS'''
class LoginPage(Screen):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)

        # Create a FloatLayout
        layout = FloatLayout()

        self.add_widget(layout)



class MyApp(App):
    def build(self):
        return LoginPage()


if __name__ == '__main__':
    MyApp().run()