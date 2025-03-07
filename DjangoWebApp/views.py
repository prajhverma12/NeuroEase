from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .speechtotext import speech_to_text  
from nltk.sentiment import SentimentIntensityAnalyzer
from django.shortcuts import render
from django.http import HttpResponse
import pyttsx3
import os


# Initialize NLTK Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def home(request):
    return render(request, "djangowebapp/texttospeech.html")  # Ensure this matches your actual template name

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