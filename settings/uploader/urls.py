from django.urls import path
from .views import *

urlpatterns = [
path ('uploader/', base,    name = 'base' ),
path('gallary/',   gallary, name ='gallary'),
path('photo/<str:pk>/', photo, name ='photo'),
path('add/',   add, name ='add'),

]