import json

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Library
@csrf_exempt
def handle(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        try:
            Library.objects.get(pk=int(data.get('bookId')))
            return JsonResponse({'ok':False})
        except Exception as e:
            print(e)
            return JsonResponse({'ok':True})

