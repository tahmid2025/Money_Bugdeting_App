from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
import sqlite3


''' THIS C;ASS IS CREATED IN ORDER FOR THE USERS TO ENTER THEIR TRANSCATIONS'''
class EditFinances(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()
        self.add_widget(layout)

        # Create a database connection
        self.conn = sqlite3.connect('Students.db')
        self.cursor = self.conn.cursor()

        # Creating the dropdown menu
        self.month_button = DropDown()
        self.item_button = DropDown()

        # Lists of months
        months = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]

        # Lists of items
        items = [
            'Food', 'Household expenses', 'Travel', 'Shopping', 'Self Care', 'Other'
        ]
