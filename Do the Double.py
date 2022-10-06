from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import pygame
import sys
    

class MyApp(App):
    def pitch(self):
        # pygame.Surface.get_pitch()
        football_pitch = BoxLayout()
        label1 = Label(text='Do the Double')
        label2 = Label(text='Username :')
        label3 = Label(text='Password :')
        button = Button(text='Submit')
        football_pitch.add_widget(label1)
        football_pitch.add_widget(label2)
        football_pitch.add_widget(label3)
        football_pitch.add_widget(button)
        return football_pitch


class MyLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.button = Button(test='Press Me')
        self.button.bind(on_press=pitch)

        self.add_widget(self.button)

class MyApp(App):
    def pitch(self, button):
        # pygame.Surface.get_pitch()
        football_pitch = BoxLayout()
        label1 = Label(text='Do the Double')
        label2 = Label(text='Username :')
        label3 = Label(text='Password :')
        button = Button(text='Submit')
        football_pitch.add_widget(label1)
        football_pitch.add_widget(label2)
        football_pitch.add_widget(label3)
        football_pitch.add_widget(button)
        return football_pitch

if __name__ == '__main__':
        MyApp().run()