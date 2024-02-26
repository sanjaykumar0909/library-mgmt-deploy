import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Library
from django.core.serializers import serialize
# @csrf_exempt
def handle(req):
    print("hi")
    data= []
    rec= Library.objects.all()
    for i in rec:
        data.append({'bookName': i.bookName, 'bookId':i.bookId, 'author': i.author, 'publishDate': i.publishDate})
    return JsonResponse(data, safe=False)
    # print(serialize('json', Library.objects.all()))