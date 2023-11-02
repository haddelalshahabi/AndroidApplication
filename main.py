from kivy.app import App
from main_layout import MainLayout
from voice_commands import initialize_voice_commands
from audio_feedback import speak


class AudioVisionApp(App):
    def build(self):
        # Initialize voice commands
        initialize_voice_commands(self.on_voice_command)

        # Welcome message and guidance
        speak("Velkommen til Audio Vision. Jeg vil guide deg gjennom appen. Bruk talekommandoer for å navigere.")

        # Set up the main layout
        self.main_layout = MainLayout()
        return self.main_layout

    def on_voice_command(self, command):
        # Handle voice commands here
        print("Voice Command:", command)
        # You can add more logic here to handle different commands


if __name__ == '__main__':
    AudioVisionApp().run()
