from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('determine/',views.do_the_math),
    path('winner/', views.celebrate),
]