from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='index2'),
    path('post/<int:post_id>/', views.details, name='details'),
]