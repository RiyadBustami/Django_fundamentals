from django.urls import path
from . import views

urlpatterns=[
    path('shows/new/',views.new_show),
    path('shows/create/',views.create_show),
    path('shows/<id>/',views.display_show),
    path('shows/',views.display_all_shows),
    path('shows/<id>/edit/',views.edit_show),
    path('shows/<id>/update/',views.update_show),
    path('shows/<id>/destroy/',views.delete_show),
    path('',views.index),
]