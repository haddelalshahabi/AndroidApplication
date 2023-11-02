from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from ui_components import SettingsButton


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Welcome Label
        self.add_widget(Label(text='Velkommen til Audio Vision!'))

        # Settings Button
        self.settings_button = SettingsButton()
        self.add_widget(self.settings_button)

        # You can add more widgets and layouts as needed
