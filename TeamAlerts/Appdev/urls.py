# Appdev/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('teams-webhook/', views.teams_webhook, name='teams_webhook'),
]
