from django.urls import path
from .views import hello_view, home_view

urlpatterns = [
    path('', home_view),        # Homepage at `/`
    path('hello/', hello_view)  # Message at `/hello/`
]


