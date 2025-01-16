from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView
)


urlpatterns = [
    path('/list-category', CategoryListView.as_view(), name='list-category'),
    path('/create-category', CategoryCreateView.as_view(), name='create-category')
    
]
