from django.urls import path
from .views import home, convert_speech, analyze_sentiment, text_to_speech_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('check_emotion_and_redirect/', views.check_emotion_and_redirect, name='check_emotion_and_redirect'),
    path("home", home, name="home"),
    path("convert-speech/", convert_speech, name="convert_speech"),
    path("analyze-sentiment/", analyze_sentiment, name="analyze_sentiment"),
    path('text-To-speech/', text_to_speech_view, name='text_To_speech'),
    path('speech-to-text/', views.speechToText, name='speech_to_text'),
    path('text-to-speech/', views.texToSpeech, name='text_to_speech'),
    path('text-sentiment/', views.texSentiment, name='text_sentiment'),

]
