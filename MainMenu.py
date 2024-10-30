from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput  
from kivy.uix.button import Button

''' THIS CLASS IS CREATED FOR THE USER TO NAVIGATE 
    AFTER THEY HAVE ENTERED THE MAIN PART OF THE PROGRAM'''
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        layout = FloatLayout()
        self.add_widget(layout)

        # First Button
        first_button = self.create_modern_button('Edit finances', pos_hint={'center_x': 0.5, 'top': 0.8})
        layout.add_widget(first_button)

        # Second Button
        second_button = self.create_modern_button('View finances', pos_hint={'center_x': 0.5, 'top': 0.65})
        layout.add_widget(second_button)



    #This method is used to create a more modern look to the buttons
    def create_modern_button(self, text, pos_hint):
        button = Button(
            text=text,
            size_hint=(None, None),
            size=(300, 75),
            pos_hint=pos_hint,
            background_normal='',  # Uses the custom background
            background_color=(0.2, 0.6, 0.8, 1),  # Button color
            color=(1, 1, 1, 1),  # Text color (white)
            bold=True,
            font_size='16sp'
        )

        return button





class MyApp(App):
    def build(self):
        return MainMenu()

if __name__ == '__main__':
    MyApp().run()

