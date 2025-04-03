import cv2
import numpy as np
import pyttsx3
from collections import deque
from django.http import JsonResponse, StreamingHttpResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from nltk.sentiment import SentimentIntensityAnalyzer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from .speechtotext import speech_to_text

# Constants
MODEL_PATH = 'djangowebapp/face_model.h5'
CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
CLASS_NAMES = ['Angry', 'Disgusted', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Load model and cascade once at the top
model_best = load_model(MODEL_PATH)
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.emotion_history = deque(maxlen=10)  # Store the last 10 emotions
        self.stable_emotion = None

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Extract the face region
            face_roi = frame[y:y + h, x:x + w]
            face_image = self._preprocess_face(face_roi)

            # Predict emotion using the loaded model
            predictions = model_best.predict(face_image)
            emotion_label = CLASS_NAMES[np.argmax(predictions)]
            print(emotion_label)

            # Add the emotion label to the history
            self.emotion_history.append(emotion_label)

            # Determine the most frequent emotion in the history
            self.stable_emotion = max(set(self.emotion_history), key=self.emotion_history.count)

            # Display the emotion label on the frame
            cv2.putText(frame, f'Emotion: {emotion_label}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (0, 0, 255), 2)

            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
    
    def _preprocess_face(self, face_roi):
        face_image = cv2.resize(face_roi, (48, 48))
        face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
        face_image = image.img_to_array(face_image)
        face_image = np.expand_dims(face_image, axis=0)
        return np.vstack([face_image])

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def index(request):
    return render(request, 'djangowebapp/index.html') # Keep this as it is


def check_emotion_and_redirect(request):
    """
    Check the stable emotion and redirect if it's 'Happy'.
    """
    camera = VideoCamera()
    camera.get_frame()  # Update stable emotion

    if camera.stable_emotion == "Happy":
        return JsonResponse({"redirect": True, "url": reverse('home')})
    return JsonResponse({"redirect": False})


# Initialize NLTK Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def home(request):
    return render(request, "djangowebapp/texttospeech.html")  # Ensure this matches your actual template name

def speechToText(request):
    return render(request, "djangowebapp/LiveSpeech-to-Text.html")

def texToSpeech(request):
    return render(request, "djangowebapp/Text-to-Speech.html")

def texSentiment(request):
    return render(request, "djangowebapp/TextSentimentAnalysis.html")

# Speech-to-Text Function
def convert_speech(request):
    if request.method == "POST":
        text = speech_to_text()  # Calls your existing speech-to-text function
        return JsonResponse({"text": text})

    return JsonResponse({"error": "Invalid request"}, status=400)  # Handle non-POST requests

# Sentiment Analysis Function
@csrf_exempt
def analyze_sentiment(request):
    if request.method == "POST":
        text = request.POST.get("text", "").strip()
        if not text:
            return JsonResponse({"error": "No text provided"}, status=400)

        # Sentiment Analysis
        scores = sia.polarity_scores(text)
        compound = scores["compound"]

        # Classify Sentiment
        if compound >= 0.05:
            sentiment = "Positive"
        elif compound <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return JsonResponse({"sentiment": sentiment})

    return JsonResponse({"error": "Invalid request"}, status=400)


# texttospeech
@csrf_exempt
def text_to_speech_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 1.0)
            engine.save_to_file(text, 'output.mp3')
            engine.runAndWait()
            with open('output.mp3', 'rb') as f:
                response = HttpResponse(f.read(), content_type='audio/mpeg')
                response['Content-Disposition'] = 'attachment; filename="output.mp3"'
                return response
    return render(request, 'texttospeech.html')