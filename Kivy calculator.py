from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('kivy', 'window_icon', 'C:\\Users\\Adil\\Desktop\\SALAD\\Calc2.png')
Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 400)
Config.set("graphics", "height", 500)


class CalculatorApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ""

        self.formula += str(instance.text)
        self.update_label()

    def clean_all(self, instance):
            self.formula = ""
            self.update_label()

    def operation(self, instance):
        array_of_operators = ["/", "X", "+", "-"]
        array_of_skobok = ["(", ")"]

        if (self.formula[len(self.formula) - 1].isdigit() is True) and (str(instance.text) in array_of_operators):
            self.formula += str(instance.text)

        if (self.formula[len(self.formula) - 1] in array_of_operators) and str(instance.text) in array_of_operators:
            temp = self.formula[:-1] + str(instance.text)
            self.formula = ""
            self.formula += temp

        if (self.formula[len(self.formula) - 1] in array_of_operators) and str(instance.text) in array_of_skobok:
            self.formula += str(instance.text)
        elif(self.formula[len(self.formula) - 1] in array_of_skobok) and str(instance.text) in array_of_skobok:
            self.formula += str(instance.text)

        if (self.formula[len(self.formula) - 1] in array_of_skobok) and str(instance.text) in array_of_operators:
            self.formula += str(instance.text)

        if (self.formula[len(self.formula) - 1].isdigit() is True) and (str(instance.text == ")")):
            self.formula += str(instance.text)




        self.update_label()

    def calc_result(self, instance):
        clean_text = ""
        for each in str(self.lbl.text):
            if each == "X":
                clean_text += "*"
            else:
                clean_text += each
        try:                                              #Handling multiple operators and Zero Division
            self.lbl.text = str(eval(clean_text))
        except Exception:
            self.lbl.text = str("Error")

        self.formula = "0"

    def build(self):

        self.load_kv("KivyLanguage.kv")  #Connect .kv with python script
        title = "Calculator"

        self.formula = "0"

        box = BoxLayout(orientation="vertical", padding=25)       #Box
        grid = GridLayout(cols=4, spacing=3, size_hint=(1, .6))   #Grid

        self.lbl = Label(text="0",
                         font_size=40,
                         size_hint=(1, .4),
                         halign="right",
                         valign="center",
                         text_size=(350, 500 * .4 - 50))

        box.add_widget(self.lbl)

        grid.add_widget(Button(text="1", on_press=self.add_number))
        grid.add_widget(Button(text="2", on_press=self.add_number))
        grid.add_widget(Button(text="3", on_press=self.add_number))
        grid.add_widget(Button(text="+", on_press=self.operation))

        grid.add_widget(Button(text="4", on_press=self.add_number))
        grid.add_widget(Button(text="5", on_press=self.add_number))
        grid.add_widget(Button(text="6", on_press=self.add_number))
        grid.add_widget(Button(text="-", on_press=self.operation))

        grid.add_widget(Button(text="7", on_press=self.add_number))
        grid.add_widget(Button(text="8", on_press=self.add_number))
        grid.add_widget(Button(text="9", on_press=self.add_number))
        grid.add_widget(Button(text="/", on_press=self.operation))

        grid.add_widget(Button(text=".", on_press=self.add_number))
        grid.add_widget(Button(text="0", on_press=self.add_number))
        grid.add_widget(Button(text="=", on_press=self.calc_result))
        grid.add_widget(Button(text="X", on_press=self.operation))
        grid.add_widget(Button(text="C", on_press=self.clean_all))
        grid.add_widget(Button(text="(", on_press=self.operation))
        grid.add_widget(Button(text=")", on_press=self.operation))



        box.add_widget(grid)
        return box


CalculatorApp().run()

