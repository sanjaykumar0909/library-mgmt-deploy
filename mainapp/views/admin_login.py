import json
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Admins
@csrf_exempt
def handle(req):
    if req.method== 'POST':
        try:
            formData= json.loads(req.body)
            print(formData)
            admin= Admins.objects.get(pk=formData.get('uname'))
            if admin and admin.pwd==formData.get('pwd'):
                return JsonResponse({'ok':True})
            else:
                return JsonResponse({'ok': False, 'err': 'pwd'})

        except:
            return JsonResponse({'ok': False,'err': 'uname'})
    else:
        return HttpResponse("Only POST", status=400)