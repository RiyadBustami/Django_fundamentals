from django.urls import path
from . import views

urlpatterns=[
    path('',views.go_to_gold),
    path('Gold/',views.gold),
    path('Gold/process_money/',views.process_money)
]