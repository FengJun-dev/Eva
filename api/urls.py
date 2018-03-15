from django.urls import path
from api import views


app_name = 'api'
urlpattern = [
    path('', views.category_list, name='category_list'),
]