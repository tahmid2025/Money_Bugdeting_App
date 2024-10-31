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
        login_button.bind(on_press=self.check_database)
        layout.add_widget(login_button)

    #This checks the database for the exisitng users
    def check_database(self, *args):
        username = self.student_username_box.text
        password = self.student_password_box.text

        # Checks if username or password fields are empty
        if not username or not password:
            self.show_error("Error", "Username or password cannot be empty.")
            return

        # Checks if the user exists in the database
        self.cursor.execute("SELECT * FROM Students WHERE username = ? AND password = ?", (username, password))
        result = self.cursor.fetchone()


        if result:
            # User found, login successful
            self.switch_to_main_menu()
        else:
            # User not found, show error popup
            self.show_error("Error", "Invalid username or password.")



    def show_error(self, title, message):
        # Create a layout for the popup
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add the error message label
        content = Label(text=message)
        layout.add_widget(content)

        # Add a close button to the popup
        close_button = Button(text="Close", size_hint=(None, None), size=(100, 50))
        layout.add_widget(close_button)

        # Create the popup and add the layout
        self.popup = Popup(title=title, content=layout, size_hint=(0.6, 0.4))
        
        # Bind the close button to dismiss the popup
        close_button.bind(on_press=self.popup.dismiss)
        
        # Open the popup
        self.popup.open()




    def switch_to_main_menu(self, *args):
        # Pass the username to the main menu and switch screens
        username = self.student_username_box.text  # Get the username from the input
        self.manager.get_screen('main_menu').set_username(username)  # Assuming MainMenu has a set_username method
        self.manager.current = 'main_menu'




class MyApp(App):
    def build(self):
        return LoginPage()


if __name__ == '__main__':
    MyApp().run()