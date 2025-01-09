from django.urls import path

from user.views import UserLoginView, UserRegistrationView, sentOtpView, VerifyOtpView

urlpatterns = [
    path("/user-registration", UserRegistrationView.as_view(), name="user-registration"),
    path("/user-login", UserLoginView.as_view(), name="user-login"),
    path("/send-otp", sentOtpView.as_view(), name="send-otp"),
    path("/verify-otp", VerifyOtpView.as_view(), name="verify-otp"),
]   