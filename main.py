from kivy.app import App
from main_layout import MainLayout
from voice_commands import initialize_voice_commands
from audio_feedback import speak
from gallery_access import Gallery

class AudioVisionApp(App):
    def build(self):
        # Initialize voice commands
        initialize_voice_commands(self.on_voice_command)

        # Initialize gallery
        self.gallery = Gallery()

        # Set gallery path manually for testing
        test_gallery_path = "/Users/haddelalshahabi/Desktop/Images"
        if not self.gallery.set_gallery_path(test_gallery_path):
            print("Failed to set gallery path. Using default path.")

        # Welcome message and guidance
        speak("Velkommen til Audio Vision. Jeg vil guide deg gjennom appen. Bruk talekommandoer for å navigere.")

        # Set up the main layout
        self.main_layout = MainLayout()
        return self.main_layout

    def on_voice_command(self, command):
        if "galleri" in command:
            folders = self.gallery.get_folders()
            speak("Her er mappene i galleriet ditt: " + ", ".join(folders))
        elif "åpne" in command:
            folder_name = command.split("åpne", 1)[1].strip()
            if self.gallery.set_folder(folder_name):
                speak("Du er nå inne i mappen " + folder_name)
            else:
                speak("Beklager, jeg kunne ikke finne mappen " + folder_name)
        elif "nyeste bilde" in command:
            latest_image = self.gallery.get_latest_image()
            if latest_image:
                speak("Her er det nyeste bildet: " + latest_image)
            else:
                speak("Det er ingen bilder i denne mappen.")
        elif "jeg vil se bildet fra" in command:
            date_query = command.split("jeg vil se bildet fra", 1)[1].strip()
            images = self.gallery.get_images_by_date(date_query)
            if images:
                speak("Her er bildene fra " + date_query + ": " + ", ".join(images))
            else:
                speak("Beklager, jeg kunne ikke finne bilder fra " + date_query)

if __name__ == '__main__':
    AudioVisionApp().run()