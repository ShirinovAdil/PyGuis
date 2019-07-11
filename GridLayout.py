from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.gridlayout import GridLayout



class GridApp(App):
    def build(self):
        grid = GridLayout(rows=2, cols=40)

        for i in range(50):

            grid.add_widget(Button(text="Adil"))
            # grid.add_widget(Button(text="Fuck"))
            # grid.add_widget(Button(text="Yourself"))
            # grid.add_widget(Button(text="Bitch"))

        return grid


GridApp().run()
