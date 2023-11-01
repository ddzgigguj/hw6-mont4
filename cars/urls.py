from django.urls import path
from . import views

urlpatterns = [
    path('post_link/', views.postView, name='posts'),
]