from django.urls import path
from .views import (
    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    # CustomerDetailView
)

urlpatterns = [
    path('/list-customers', CustomerListView.as_view(), name='customer-list'),
    path('/create-customer', CustomerCreateView.as_view(), name='customer-create'),
    path('/update-customer', CustomerUpdateView.as_view(), name='customer-update'),
    path('/delete-customer', CustomerDeleteView.as_view(), name='customer-delete'),
    # path('/customer-detail', CustomerDetailView.as_view(), name='customer-detail')
]