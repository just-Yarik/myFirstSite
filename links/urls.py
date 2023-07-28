from django.urls import path
from .views import shorten_url
from . import views

app_name = 'links'

urlpatterns = [
    path('shorten/', views.shorten_url, name='shorten_url'),
]
