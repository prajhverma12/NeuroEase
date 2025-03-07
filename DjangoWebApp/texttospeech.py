import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Test it (Optional)
if __name__ == '__main__':
    text_to_speech("Hello! This is a text-to-speech conversion example.")
