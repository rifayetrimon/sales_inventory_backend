from django.urls import path

from user.views import UserLoginView, UserRegistrationView

urlpatterns = [
    path("/user-registration", UserRegistrationView.as_view(), name="user-registration"),
    path("/user-login", UserLoginView.as_view(), name="user-login"),
]   