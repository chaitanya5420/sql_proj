from django.urls import path
from .views import *

urlpatterns = [
# path('base', base, name='base'),
path('gallary/'        ,   gallary      , name ='gallary'),
path('photo/<str:pk>/' ,   photo        , name ='photo'),
path('add/'            ,   add          , name ='add'),
path('file_upload'     ,   upload_file  , name='file_upload'),
path('view_files', view_files, name='view')
]