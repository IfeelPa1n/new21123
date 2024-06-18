from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Announcement
import json

@csrf_exempt
def teams_webhook(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body.decode('utf-8'))
            title = payload['title']
            content = payload['text']
            announcement = Announcement.objects.create(title=title, content=content)
            return JsonResponse({'message': 'Announcement received and stored successfully'})
        except KeyError:
            return JsonResponse({'error': 'Invalid payload format'}, status=400)
    else:
        return JsonResponse({'error': 'POST request required'}, status=405)
