from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.modules import keybinding
from kivy.core.window import Window
import re
import requests

Config.set("graphics", "resizable", 0)


class Widgets(Widget):

    def find_time(self):

        url = 'https://www.timeanddate.com/worldclock/'
        self.ids.country.text = self.ids.country.text.lower()
        self.ids.city.text = self.ids.city.text.lower()
        req = requests.get(url + str(self.ids.country.text) + "/" + str(self.ids.city.text))
        out = req.text

        filtered = re.findall(r'..:..:..', out)
        if len(filtered) > 0:
            print("Current local time in {}, {} is\n {}".format(self.ids.country.text, self.ids.city.text, filtered))
            self.ids.status_bar.text += ("Current local time in {}, {} is\n {}".format(self.ids.country.text, self.ids.city.text, filtered))
        else:
            print("Make sure you entered the info correctly")
            self.ids.status_bar.text += ("Incorrect info or not found")


class TimeApp(App):

    def build(self):
        self.load_kv("time_gui.kv")
        to_return = Widgets()
        return to_return


TimeApp().run()
