from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('add-ticket/', add_ticket, name='add_ticket'),
]
