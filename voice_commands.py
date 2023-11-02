import threading
import speech_recognition as sr

recognizer = sr.Recognizer()

def initialize_voice_commands(callback):
    def listen():
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            print("Say something!")
            while True:
                try:
                    audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(audio, language='no-NO')
                    print("Voice Command:", command)
                    callback(command)
                except sr.WaitTimeoutError:
                    print("Listening timed out, trying again...")
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))

    # Start listening in a separate thread
    threading.Thread(target=listen).start()
