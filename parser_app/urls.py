from django.urls import path
from . import views

urlpatterns = [
    path('Olx_list_parser/', views.ParserOlxListView.as_view()),
    path('start_parsing/', views.ParserFormView.as_view()),
]