from kivy.app import App # this helps run the application 
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.floatlayout import FloatLayout # helps with the layout
from kivy.uix.button import Button
from kivy.uix.image import Image



''' This class is the main starting page for the program
 it will include the logo, the login and sign in button'''
class StartPage(Screen):
    def __init__(self, **kwargs):
        super(StartPage, self).__init__(**kwargs)
        layout = FloatLayout()  # Switchs to FloatLayout for custom positioning
        self.add_widget(layout)# This diplays the page


        # Buttons for sign up and login
        signup_button = Button(text='Sign up page', size_hint=(None, None), size=(200, 50),
                               pos_hint={'center_x': 0.5, 'y': 0.9})  # Centeres horizontally, 50% up from bottom
        signup_button.bind(on_press=self.switch_to_signup)
        layout.add_widget(signup_button)# this displays the button
     

        login_button = Button(text='Login page', size_hint=(None, None), size=(200, 50),
                              pos_hint={'center_x': 0.5, 'y': 0.8})  # Centered horizontally, 30% up from bottom
        login_button.bind(on_press=self.switch_to_login)
        layout.add_widget(login_button)

        # Add image at the top
        logo_image = Image(source='logo.jpeg', size_hint=(0.7, 0.7), pos_hint={'center_x': 0.5, 'top': 0.75})
        layout.add_widget(logo_image)



    def switch_to_signup(self, *args):
        self.manager.current = 'signup'

    def switch_to_login(self, *args):
        self.manager.current = 'login'


class MyApp(App):
    def build(self):
        # Creates a ScreenManager
        self.title = 'Tahmids budgeting App' # This is the title of the window

        sm = ScreenManager()
        

        # Add screens
        sm.add_widget(StartPage(name='start'))
        return sm


if __name__ == '__main__':
    MyApp().run()
