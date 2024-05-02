import speech_recognition as sr
from gtts import gTTS
import os
from gtts import gTTS
from playsound import playsound

def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    playsound("output.mp3")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Request error: {e}")
    return ""

# def speak(text, lang='en'):
#     tts = gTTS(text=text, lang=lang)
#     tts.save("output.mp3")
#     os.system("mpg321 output.mp3")  # Use mpg321 for Linux or macOS, use mpg123 for Windows

def main():
    while True:
        print("\nPress 'q' to quit.")
        text = listen()
        if text.lower() == 'q':
            print("Goodbye!")
            break
        if text:
            print("You said:", text)
            speak(text)

if __name__ == "__main__":
    main()
