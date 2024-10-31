from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput  
from kivy.uix.button import Button
import sqlite3
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

'''THIS CLASS IS CREATED TO ALLOW EXISTING USERS TO LOG INTO THEIR ACCOUNTS'''
class LoginPage(Screen):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)

        # Create a FloatLayout
        layout = FloatLayout()
        self.add_widget(layout)

        # Create a database connection
        self.conn = sqlite3.connect('Students.db')
        self.cursor = self.conn.cursor()




        # Adds username label
        layout.add_widget(Label(text='Username', size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.5, 'top': 0.9}))

        # Adds text input for username
        self.student_username_box = TextInput(multiline=False, size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'top': 0.85})
        layout.add_widget(self.student_username_box)

        # Adds password label
        layout.add_widget(Label(text='Password', size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.5, 'top': 0.775}))

        # Adds text input for password
        self.student_password_box = TextInput(multiline=False, password=True, size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'top': 0.725})
        layout.add_widget(self.student_password_box)

        # Adds login button
        login_button = Button(text="Login", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'top': 0.675})
        layout.add_widget(login_button)



class MyApp(App):
    def build(self):
        return LoginPage()


if __name__ == '__main__':
    MyApp().run()