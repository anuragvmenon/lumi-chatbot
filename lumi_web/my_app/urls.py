from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatroom/', views.chatroom, name='chatroom'),
    path('track_mood/', views.track_mood, name='track_mood'),
    path('mood_analytics/', views.mood_analytics, name='mood_analytics'),
]
