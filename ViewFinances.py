from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
import sqlite3


'''THIS CLASS IS CREATED IN ORDER FOR THE USER TO VIEW THEIR MONTHLY SPENDING'''
class ViewFinances(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create layout for the screen
        self.layout = FloatLayout()
        self.add_widget(self.layout)

        # Connect to the database
        self.conn = sqlite3.connect('Students.db')
        self.cursor = self.conn.cursor()
