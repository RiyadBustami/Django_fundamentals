from django.urls import path
from . import views

urlpatterns=[
    path('',views.redirect_time),
    path('time_display/',views.show_time),
]