"""import pyttsx3

xxx=pyttsx3.init()
name=input('Enter your name please:')
xxx.say("Hello"+name)
xxx.runAndWait()
"""

"""
import pyttsx3
import speech_recognition as sr

# Initialize speech recognition & text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Capture voice input
with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
    audio = recognizer.listen(source)

# Convert speech to text
try:
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")

    # Speak the recognized text
    engine.say(f"You said: {text}")
    engine.runAndWait()

except sr.UnknownValueError:
    print("Could not understand the audio")
except sr.RequestError:
    print("Error with speech recognition service")





import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening for input...")
    recognizer.listen(source)
print("Microphone is working!")



"""