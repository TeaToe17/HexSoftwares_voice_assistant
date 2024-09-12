import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        print("here")
        if audio is not None:
            print("Audio captured.")
            with open("captured_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())
            print("Audio saved as 'captured_audio.wav'. You can play it to verify.")
        else:
            print("No audio captured.")
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Could not understand your audio, Please say that again...")
        return "None"
    return query

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How may I help you?")

def execute_task():
    greet_user()

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak(f"According to Wikipedia, {results}")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")

        elif 'open code' in query:
            code_path = "C:\\path\\to\\your\\code\\editor.exe"  # Set your code editor's path
            os.startfile(code_path)
            speak("Opening your code editor")

        elif 'quit' in query or 'exit' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    execute_task()
