from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    CategoryRetrieveView
)


urlpatterns = [
    path('/list-category', CategoryListView.as_view(), name='list-category'),
    path('/create-category', CategoryCreateView.as_view(), name='create-category'),
    path('/update-category', CategoryUpdateView.as_view(), name='update-category'),
    path('/delete-category', CategoryDeleteView.as_view(), name='delete-category'),
    path('/category-by-id/<int:pk>', CategoryRetrieveView.as_view(), name='retrieve-category'),
]
