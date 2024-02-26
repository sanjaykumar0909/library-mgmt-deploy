import json
from datetime import datetime

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Library

@csrf_exempt
def handle(req):
    if req.method == 'POST':
        book_list = json.loads(req.body)
        print("add_books")
        try:
            for book in book_list:
                publish_date= datetime.strptime(book.get('publishDate'), "%Y-%m-%d")
                Library(
                    bookId= int(book.get('bookId')),
                    bookName= book.get('bookName'),
                    author= book.get('author'),
                    publishDate= publish_date
                ).save()
            return JsonResponse({'ok':True})
        except Exception as e:
            print(e)
        print(book_list)
    return HttpResponse("only POST", status=400)