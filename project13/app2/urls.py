from django.urls import path
from app2.views import *
app_name='bb'

urlpatterns=[
    path('godfather/',godfather,name='godfather')
]