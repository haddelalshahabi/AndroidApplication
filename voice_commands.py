import speech_recognition as sr

recognizer = sr.Recognizer()

def initialize_voice_commands(callback):
    # Start listening to voice commands
    # 'callback' is a function that will be called when a command is recognized
    pass  # You need to implement this function

def listen_for_commands():
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language='no-NO')
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
