from kivy.app import App
from kivy.uix.button import Button

class MyProgram(App):

    def build(self):
        return Button(text='Olá Mundo')

MyProgram().run()
