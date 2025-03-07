from django.urls import path
from .views import home, convert_speech, analyze_sentiment, text_to_speech_view

urlpatterns = [
    path("", home, name="home"),
    path("convert-speech/", convert_speech, name="convert_speech"),
    path("analyze-sentiment/", analyze_sentiment, name="analyze_sentiment"),
    path('text-to-speech/', text_to_speech_view, name='text_to_speech'),
]
