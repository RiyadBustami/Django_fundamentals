# from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('blogs/',include("first_app.urls")),
    path('surveys/',include("surveys_app.urls")),
    path('',include("users_app.urls")),
]
