from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
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
        
        # Main button to trigger the month dropdown
        main_button1 = self.create_modern_button(text='Select Month', pos_hint={'center_x': 0.5, 'center_y': 0.9})
        layout.add_widget(main_button1)

        # Main button to trigger the item dropdown
        main_button2 = self.create_modern_button(text='Select Item', pos_hint={'center_x': 0.5, 'center_y': 0.8})
        layout.add_widget(main_button2)

        # Label for the user to enter the amount entered
        layout.add_widget(Label(text='Enter the amount you have spent in GBP(£)', size_hint=(None, None), size=(400, 30), pos_hint={'center_x': 0.5, 'top': 0.7}))
        self.student_budget_box = TextInput(multiline=False, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5, 'top': 0.65})
        layout.add_widget(self.student_budget_box)

        #Submit button
        Submit_button = self.create_modern_button(text='Submit', pos_hint={'center_x': 0.5, 'top': 0.6})
        layout.add_widget(Submit_button)


    def create_modern_button(self, text, pos_hint):
        button = Button(
            text=text,
            size_hint=(None, None),
            size=(400, 50),
            pos_hint=pos_hint,
            background_normal='',  # Use the custom background
            background_color=(0.2, 0.6, 0.8, 1),  # Button color
            color=(1, 1, 1, 1),  # Text color (white)
            bold=True,
            font_size='16sp'
        )
        return button


class MyApp(App):
    def build(self):
        return EditFinances()

if __name__ == '__main__':
    MyApp().run()




