import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        try:
            print("Start talking...")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
            audio = recognizer.listen(source)
        except OSError:
            return "Microphone not found or access denied."

        try:
            text = recognizer.recognize_google(audio, language="en-US")
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Could not request results, please check your internet connection."

# Test it (Optional)
if __name__ == '__main__':
    print(speech_to_text())  # Always listens in English (US)
