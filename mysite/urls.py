from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Django Tutorial Project</h1>
        <p>This is my deployed Django project.</p>
        <p><a href="/polls/">Go to Polls</a></p>
        <p><a href="https://github.com/MatasZos/djangotutorialproject">View Source Code on GitHub</a></p>
    """)

urlpatterns = [
    path("", home),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
] + debug_toolbar_urls()