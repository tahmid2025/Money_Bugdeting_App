from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput  
from kivy.uix.button import Button


''' THIS CLASS IS CREATED TO HELP NEW USERS TO SIGN UP TO THE PROGRAM'''
class SignupPage(Screen):
    def __init__(self, **kwargs):
        super(SignupPage,self).__init__(**kwargs)

        layout=FloatLayout()

        self.add_widget(layout)

        # Name input
        layout.add_widget(Label(text="Name:", size_hint=(None, None), size=(400, 30), pos_hint={'center_x': 0.5, 'top': 0.9}))
        self.student_name_box = TextInput(multiline=False, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5, 'top': 0.85})
        layout.add_widget(self.student_name_box)

        # Surname input
        layout.add_widget(Label(text="Surname:", size_hint=(None, None), size=(400, 30), pos_hint={'center_x': 0.5, 'top': 0.75}))
        self.student_surname_box = TextInput(multiline=False, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5, 'top': 0.7})
        layout.add_widget(self.student_surname_box)

        # Username input
        layout.add_widget(Label(text="Username:", size_hint=(None, None), size=(400, 30), pos_hint={'center_x': 0.5, 'top': 0.6}))
        self.student_username_box = TextInput(multiline=False, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5, 'top': 0.55})
        layout.add_widget(self.student_username_box)

        # Password input
        layout.add_widget(Label(text="Password:", size_hint=(None, None), size=(400, 30), pos_hint={'center_x': 0.5, 'top': 0.45}))
        self.student_password_box = TextInput(multiline=False, password=True, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5, 'top': 0.4})
        layout.add_widget(self.student_password_box)

           # Sign Up button with the same size as the StartPage buttons
        signup_button = Button(text="Sign Up", size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5, 'top': 0.3})  # Centered horizontally
        layout.add_widget(signup_button)


class MyApp(App):
    def build(self):
        return SignupPage()

if __name__ == '__main__':
    MyApp().run()





