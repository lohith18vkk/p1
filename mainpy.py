
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel

class CalculatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "A400"

        self.screen = MDScreen()
        self.grid = GridLayout(cols=4, spacing=10, size_hint=(1, .6))
        
        self.equation = ""

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            ".", "0", "=", "+",
            "C",
        ]

        # Adding display label
        self.display_label = MDLabel(font_style="H4", halign="right")
        self.screen.add_widget(self.display_label)

        for button in buttons:
            self.grid.add_widget(
                MDRaisedButton(
                    text=button,
                    on_release=self.button_pressed
                )
            )

        self.screen.add_widget(self.grid)
        return self.screen

    def button_pressed(self, instance_button):
        if instance_button.text == "=":
            try:
                self.equation = str(eval(self.equation))
            except Exception:
                self.equation = "Error"
        elif instance_button.text == "C":
            self.equation = ""
        else:
            self.equation += instance_button.text

        self.update_display()

    def update_display(self):
        self.display_label.text = self.equation

if __name__ == "__main__":
    CalculatorApp().run()
