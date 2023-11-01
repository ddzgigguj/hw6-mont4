from django.urls import path
from . import views

urlpatterns = [
    path('avtoparts_list/', views.AvtopartsListView.as_view(), name='AvtopartsList'),
    path('avtoparts_detail/<int:id>/', views.AvtopartsDetailView.as_view(), name='detail'),
    path('avtoparts_detail/<int:id>/delete/', views.DeleteProductsView.as_view(), name='delete'),
    path('avtoparts_detail/<int:id>/update/', views.UpdateProductsView.as_view(), name='update'),
    path('create_product/', views.CreateProductsView.as_view(), name='createProduct'),
    path('search/', views.Search.as_view(), name='search'),
    path('review_form/', views.FormCommentView.as_view(), name='reviewForm'),
]