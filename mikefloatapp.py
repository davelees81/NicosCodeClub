from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.floatlayout import FloatLayout
    

class MyApp(App):
    def build(self):
        layout = FloatLayout()
        label1 = Label(text='hello', size_hint=(0.2, 0.3), pos_hint={'center_x':0.2, 'center_y':0.5})
        label2 = Label(text='there', size_hint=(0.4, 0.6), pos_hint={'center_x':0.5, 'center_y':0.1})

        layout.add_widget(label1)
        layout.add_widget(label2)
        


        return layout


if __name__ == '__main__':
        MyApp().run()