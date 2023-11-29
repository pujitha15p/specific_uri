from app.views import *
from django.urls import path

app_name='clientfirst'
urlpatterns=[
    path('client/',client,name='client'),
]
