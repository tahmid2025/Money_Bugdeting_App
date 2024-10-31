from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput  
from kivy.uix.button import Button
import sqlite3
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout




''' THIS CLASS IS CREATED TO HELP NEW USERS TO SIGN UP TO THE PROGRAM'''
class SignupPage(Screen):
    def __init__(self, **kwargs):
        super(SignupPage,self).__init__(**kwargs)

        layout=FloatLayout()
        self.add_widget(layout)

        # Create a database connection
        self.conn = sqlite3.connect('Students.db')
        self.cursor = self.conn.cursor()

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
        signup_button.bind(on_press=self.update_database)
        layout.add_widget(signup_button)

    # This updates the database with the students details
    def update_database(self, *args):
        name = self.student_name_box.text
        surname = self.student_surname_box.text
        username = self.student_username_box.text
        password = self.student_password_box.text


        # Check if any fields are empty
        if not name or not surname or not username or not password:
            self.show_error("Error", "All fields must be filled.")
            return # Exit the function early if any field is empty
        
        #Checks if the username is are already in use
        self.cursor.execute("SELECT * FROM Students WHERE username = ?", (username,))
        existing_user = self.cursor.fetchone()  # Fetch one record


        if existing_user:
            self.show_error("Error", "Username already exists.")  # Show error if username exists
            return  # Exit early
        

        try:
            self.cursor.execute('''INSERT INTO Students (name, surname, username, password) 
                                   VALUES (?, ?, ?, ?)''', (name, surname, username, password))
            self.conn.commit()  # Commits the changes
            print("User signed up successfully!")  # Confirmation message
            self.switch_to_main_menu()  # Switchs to the main menu after success
        except sqlite3.Error as e:
            self.show_error("Error", str(e))  # Displays any other database errors




    #This is the display template that is used to show error screens
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


    # This swithces the screen to the mainmenu and moves the entered username to the mainmenu screen
    def switch_to_main_menu(self, *args):
        # Switch to the 'main_menu' screen
        username = self.student_username_box.text  # Get the username from the input
        self.manager.get_screen('main_menu').set_username(username)  # Pass it to MainMenu
        self.manager.current = 'main_menu'

      

    


class MyApp(App):
    def build(self):
        return SignupPage()

if __name__ == '__main__':
    MyApp().run()





