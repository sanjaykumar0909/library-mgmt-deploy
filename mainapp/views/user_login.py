import json
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handle(req):
    if req.method== 'POST':
        try:
            data= json.loads(req.body)
            print(data)
            return JsonResponse({'ok': True})
        except:
            return JsonResponse({'ok': False})
    else:
        return HttpResponse("only POST", status=400)