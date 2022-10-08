from turtle import color
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import sys


class MyLayout(FloatLayout):
    
    # def label1(self):
        # self.label1 = Label(text="Nico's App", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.2, 'center_y': 0.5})
        # self.add_widget(self.label1)
    
    def __init__(self):
        super().__init__()
        self.button = Button(text='Press Me', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.button.bind(on_press=self.new_label)
        self.button.bind(on_press=self.new_button)

        self.label1 = Label(text="Nico's App", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.9}, color=(0,0,9,1))
        # self.label1.color=(100,255,100,255)
        # self.label1.config(bg="yellow")
        self.add_widget(self.label1)

        self.add_widget(self.button)
        



    def new_label(self, button):
        self.label = Label(text='Nearly Finished', size=(50,50), size_hint=(None,None), pos=(375,275))
        self.add_widget(self.label)
        self.remove_widget(button)

    def close_app():
        sys.exit()


    def new_button(self, button):
        self.new_button = Button(text='End', size=(50,50), size_hint=(None,None), pos=(375,10))
        # self.button.bind(on_press=self.new_button)
        self.add_widget(self.new_button)
        self.new_button.bind(on_press=self.close_app())


    
        
        


class MyApp(App):    
      def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()