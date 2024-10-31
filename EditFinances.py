from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

''' THIS C;ASS IS CREATED IN ORDER FOR THE USERS TO ENTER THEIR TRANSCATIONS'''
class EditFinances(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
        self.add_widget(layout)

        # Create a database connection
        self.conn = sqlite3.connect('Students.db')
        self.cursor = self.conn.cursor()