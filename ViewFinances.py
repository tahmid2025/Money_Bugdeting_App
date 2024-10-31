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
        self.student_id=None

    #Stores the username and fetches the corresponding student ID
    def set_username(self, username):
        self.username = username
        self.get_student_id()

    #Fetches the student_id based on the username."""
    def get_student_id(self):
        self.cursor.execute("SELECT student_id FROM Students WHERE username = ?", (self.username,))
        result = self.cursor.fetchone()

        #This Checks if a result was returned from the query
        if result:
            self.student_id = result[0]
            self.show_finances(self.student_id)

    #Fetches and displays the student's financial data in a bar chart
    def show_finances(self, student_id):
        """Fetches and displays the student's financial data in a bar chart."""
        # Fetch data for the graph
        self.cursor.execute("SELECT month, food, household_expenses, travel, shopping, self_care, other FROM Items WHERE student_id = ?", (student_id,))
        data = self.cursor.fetchall()

        if not data:
            print("No data found for this student.")
            return
        
        