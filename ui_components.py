from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class SettingsButton(Button):
    def __init__(self, **kwargs):
        super(SettingsButton, self).__init__(**kwargs)
        self.text = "Settings"
        self.size_hint = (None, None)
        self.size = (200, 50)
        self.pos_hint = {'center_x': 0.5}
        self.bind(on_press=self.open_settings)

    def open_settings(self, instance):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Settings go here'))
        popup = Popup(title='Settings', content=content, size_hint=(None, None), size=(300, 300))
        popup.open()