from django.urls import path
from .views import *

urlpatterns = [
path('base', base, name='base'),

path('gallary/'        ,   gallary      , name ='gallary'),
path('photo/<str:pk>/' ,   photo        , name ='photo'),
path('add/'            ,   add          , name ='add'),
path('photo/<int:pk>/delete/',delete_photo, name='delete_photo'),

path('file_upload/', upload_file, name='file_upload'),
path('view_files',   view_files, name='view'),
path('show_tables/<int:file_id>/', show_tables, name='show_tables')
]