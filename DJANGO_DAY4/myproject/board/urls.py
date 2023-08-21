from django.urls import path
from . import views

urlpatterns = [
    path('',views.read_Post_data, name='index'),
    path('add_page',views.add_Post_data, name='add_data')
]
