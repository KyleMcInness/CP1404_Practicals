"""..."""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

CONVERSION_RATE = 1.60934


class ConvertMilesApp(App):
    message = StringProperty()

    def build(self):

        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("miles_to_kilometres.kv")
        return self.root

    def handle_increment(self, value):

        if self.root.ids.input_text.text == "":
            self.root.ids.input_text.text = "0"

        number = int(self.root.ids.input_text.text)
        number += value
        self.root.ids.input_text.text = str(number)

    def conversion(self):

        try:
            miles = int(self.root.ids.input_text.text)
        except ValueError:
            miles = 0

        if miles <= 0:
            self.root.ids.output_text.text = "0.0"
        else:
            kilometres = miles * CONVERSION_RATE
            self.root.ids.output_text.text = str(kilometres)

    def handle_press(self):
        self.message = self.root.ids.input_text.text


ConvertMilesApp().run()
