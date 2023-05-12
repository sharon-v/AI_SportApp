from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from testing import squatDetect


def callback(instance):
    print("The button has been pressed")
    squatDetect()


class AthleticInteligence(MDApp):
    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "DeepOrange"
        screen = MDScreen()

        # toolbar top
        self.toolbar = MDTopAppBar(
            title="Athletic Intelligence",
            pos_hint={"top": 1})
        screen.add_widget(self.toolbar)

        # logo image
        screen.add_widget(Image(
            source="logo.png",
            pos_hint={"center_x": 0.5, "center_y": 0.7}))

        # label welcome
        self.label = MDLabel(
            text="Welcome to Athletic Intelligence",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Primary",
            font_style="H5")
        screen.add_widget(self.label)

        # button squat
        screen.add_widget(MDFillRoundFlatButton(
            text="Start Training",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=callback))
        return screen


if __name__ == "__main__":
    AthleticInteligence().run()
