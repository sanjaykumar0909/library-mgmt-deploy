from django.urls import path
from .views import user_login, library, admin_login, can_add_book, add_books

urlpatterns=[
    path('', user_login.handle),
    path('admin/', admin_login.handle),
    path('can-add-book/', can_add_book.handle),
    path('library', library.handle),
    path('add-books/', add_books.handle)
]