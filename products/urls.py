from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductDetailView
)

urlpatterns = [
    path('/list-product', ProductListView.as_view(), name='list-product'),
    path('/create-product', ProductCreateView.as_view(), name='create-product'),
    path('/update-product', ProductUpdateView.as_view(), name='update-product'),
    path('/delete-product', ProductDeleteView.as_view(), name='delete-product'),
    path('/detail-product/<int:pk>', ProductDetailView.as_view(), name='detail-product')
]
    