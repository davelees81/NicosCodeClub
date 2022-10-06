from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
    

class MyApp(App):
    def build(self):
        layout = FloatLayout()
        button1 = Button(text='Press Me', size=(100,100), size_hint=(None, None), pos=(500,100))
        # label2 = Label(text='there', size_hint=(0.4, 0.6), pos_hint={'center_x':0.5, 'center_y':0.1})

        layout.add_widget(button1)
        # layout.add_widget(label2)
        


        return layout


if __name__ == '__main__':
        MyApp().run()