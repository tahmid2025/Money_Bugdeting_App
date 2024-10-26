from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout



class StartPage(Screen):
    def __init__(self, **kwargs):
        super(StartPage, self).__init__(**kwargs)
        layout = FloatLayout()  # Switch to FloatLayout for custom positioning

        self.add_widget(layout)
     


if __name__ == '__main__':
    StartPage().run()
