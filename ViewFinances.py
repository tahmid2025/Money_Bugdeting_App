from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
import sqlite3
import plotly.graph_objects as go
import plotly.io as pio
from kivy.uix.image import Image



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
        # Fetch data for the graph
        self.cursor.execute("SELECT month, food, household_expenses, travel, shopping, self_care, other FROM Items WHERE student_id = ?", (student_id,))
        data = self.cursor.fetchall()

        if not data:
            print("No data found for this student.")
            return
        

                # Prepare data for plotting
        months = [row[0] for row in data]
        food_expenses = [row[1] for row in data]
        household_expenses = [row[2] for row in data]
        travel_expenses = [row[3] for row in data]
        shopping_expenses = [row[4] for row in data]
        self_care_expenses = [row[5] for row in data]
        other_expenses = [row[6] for row in data]

        # Create a bar chart with Plotly
        fig = go.Figure()
        fig.add_trace(go.Bar(x=months, y=food_expenses, name='Food'))
        fig.add_trace(go.Bar(x=months, y=household_expenses, name='Household'))
        fig.add_trace(go.Bar(x=months, y=travel_expenses, name='Travel'))
        fig.add_trace(go.Bar(x=months, y=shopping_expenses, name='Shopping'))
        fig.add_trace(go.Bar(x=months, y=self_care_expenses, name='Self Care'))
        fig.add_trace(go.Bar(x=months, y=other_expenses, name='Other'))

        # Update layout
        fig.update_layout(
            title=f'{self.username} Your Monthly Expenses by Category',
            xaxis_title='Month',
            yaxis_title='Expenses',
            barmode='group'
        )

        # Save plot as an image
        pio.write_image(fig, 'expenses_chart.png')  # Save image as PNG

        img = Image(source='expenses_chart.png', size_hint=(1, 0.95), allow_stretch=True, keep_ratio=False)  # Set size_hint to (1, 1)
        self.layout.add_widget(img)
        
        