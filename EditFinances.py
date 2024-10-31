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
        
                # Add each month as a button in the dropdown
        for month in months:
            month_btn = Button(text=month, size_hint_y=None, height=44)
            month_btn.bind(on_release=lambda btn: self.set_month(main_button1, btn.text))  # Directly bind to set_month
            self.month_button.add_widget(month_btn)

        # Add each item as a button in the dropdown
        for item in items:
            item_btn = Button(text=item, size_hint_y=None, height=44)
            item_btn.bind(on_release=lambda btn: self.set_item(main_button2, btn.text))  # Directly bind to set_item
            self.item_button.add_widget(item_btn)


        # Main button to trigger the month dropdown
        main_button1 = self.create_modern_button(text='Select Month', pos_hint={'center_x': 0.5, 'center_y': 0.9})
        main_button1.bind(on_release=self.month_button.open)  # Open the dropdown when the button is pressed
        layout.add_widget(main_button1)

        # Main button to trigger the item dropdown
        main_button2 = self.create_modern_button(text='Select Item', pos_hint={'center_x': 0.5, 'center_y': 0.8})
        main_button2.bind(on_release=self.item_button.open)  # Open the dropdown when the button is pressed
        layout.add_widget(main_button2)

        # Label for the user to enter the amount entered
        layout.add_widget(Label(text='Enter the amount you have spent in GBP(£)', size_hint=(None, None), size=(400, 30), pos_hint={'center_x': 0.5, 'top': 0.7}))
        self.student_budget_box = TextInput(multiline=False, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5, 'top': 0.65})
        layout.add_widget(self.student_budget_box)

        #Submit button
        Submit_button = self.create_modern_button(text='Submit', pos_hint={'center_x': 0.5, 'top': 0.6})
        layout.add_widget(Submit_button)


    # This is used to move the username from the mainmenu to the current screren which will be used later
    def set_username(self,username):
        self.username=username # this hold the value of the username thats been transferred by the mainmenu

    # This function is used to set the selected month from the dropdown
    def set_month(self, button, month):
        self.selected_month = month  # Store the selected month
        button.text = month  # Change button text
        self.month_button.dismiss()  # Close the dropdown

   # This function is used to set the selected item from the dropdown
    def set_item(self, button, item):
        self.selected_item = item  # Store the selected item
        button.text = item  # Change button text
        self.item_button.dismiss()  # Close the dropdown

    # This function is used to update the database when submit button is clicked 
    def update_database(self, *args):
        month = self.selected_month
        item = self.selected_item
        amount = self.student_budget_box.text

        #This is used to get the users student iD using the retrived username from the method above
        self.cursor.execute("SELECT student_id FROM Students WHERE username = ?", (self.username,))
        result1 = self.cursor.fetchone()
        
        # This ensure result1 is not None and extract student_id
        if result1:
            student_id = result1[0]  # Get the first element of the tuple

        # Check if a record for the month already exists
        self.cursor.execute("SELECT * FROM Items WHERE student_id = ? AND month = ?", (student_id, month))
        result2 = self.cursor.fetchone()

        # This checks which item has been chosen by the user and then updates the amount accordingly 
        if result2:
            print("Record already exists for this month:", result2)
            # Update the existing record with the new amount  
            if item == 'Food':
                self.cursor.execute("UPDATE Items SET food = food + ? WHERE student_id = ? AND month = ?", (amount, student_id, month))
            elif item == 'Household expenses':
                self.cursor.execute("UPDATE Items SET household_expenses = household_expenses + ? WHERE student_id = ? AND month = ?", (amount, student_id, month))
            elif item == 'Travel':
                self.cursor.execute("UPDATE Items SET travel = travel + ? WHERE student_id = ? AND month = ?", (amount, student_id, month))
            elif item == 'Shopping':
                self.cursor.execute("UPDATE Items SET shopping = shopping + ? WHERE student_id = ? AND month = ?", (amount, student_id, month))
            elif item == 'Self Care':
                self.cursor.execute("UPDATE Items SET self_care = self_care + ? WHERE student_id = ? AND month = ?", (amount, student_id, month))
            elif item == 'Other':
                self.cursor.execute("UPDATE Items SET other = other + ? WHERE student_id = ? AND month = ?", (amount, student_id, month))
            self.conn.commit()  # Commit the changes

            print(f"Record updated for {month} with student_id {student_id} for {item} by amount {amount}.")
        else:
            # This inserts a new record since it doesn't exist and then creates creates a record with placeholder values for the other fields (assuming they're numeric)
            values = {
                'food': 0,
                'household_expenses': 0,
                'travel': 0,
                'shopping': 0,
                'self_care': 0,
                'other': 0
            }
            values[item.lower().replace(" ", "_")] = amount  # Set the correct field to the amount

            self.cursor.execute('''INSERT INTO Items (student_id, month, food, household_expenses, travel, shopping, self_care, other)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                                (student_id, month, values['food'], values['household_expenses'], 
                                values['travel'], values['shopping'], 
                                values['self_care'], values['other']))

            self.conn.commit()  # Commit the changes
            print(f"New record created for {month} with student_id {student_id} and {item}.")



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




