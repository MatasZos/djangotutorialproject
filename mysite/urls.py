from django.urls import include, path
from django.contrib import admin
from django.shortcuts import redirect

def home(request):
    return redirect("polls:index")

urlpatterns = [
    path("", home),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]