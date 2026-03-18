from django.shortcuts import render
from django.http import JsonResponse
from .models import Mood
import json

def index(request):
    return render(request, 'index.html')

def track_mood(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        emotion = data.get('emotion')
        if user_id and emotion:
            mood = Mood.objects.create(user_id=user_id, emotion=emotion)
            return JsonResponse({'status': 'success', 'mood_id': mood.id})
        return JsonResponse({'status': 'error', 'message': 'user_id and emotion are required'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def mood_analytics(request):
    user_id = request.GET.get('user_id')
    if user_id:
        moods = Mood.objects.filter(user_id=user_id).order_by('timestamp')
        return render(request, 'mood_analytics.html', {'moods': moods})
    return render(request, 'mood_analytics.html', {'moods': []})
