from django.urls import path
from . import views

urlpatterns=[
    path('',views.books_index),
    path('add_new_book/',views.add_new_book),
    path('books/<id>/',views.books_show),
    path('books/<id>/add_author/',views.add_author),
    path('authors/',views.authors_index),
    path('authors/add_new_author/',views.add_new_author),
    path('authors/<id>/',views.authors_show),
    path('authors/<id>/add_book/',views.add_book),
]