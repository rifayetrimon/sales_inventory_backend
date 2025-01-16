from django.urls import path

from user.views import (
    UserLoginView, 
    UserRegistrationView, 
    sentOtpView, 
    VerifyOtpView, 
    ResetPasswordView,
    UserProfileView,
    UserProfileUpdateView,
    UserLogoutView
)




urlpatterns = [
    path("/user-registration", UserRegistrationView.as_view(), name="user-registration"),
    path("/user-login", UserLoginView.as_view(), name="user-login"),
    path("/send-otp", sentOtpView.as_view(), name="send-otp"),
    path("/verify-otp", VerifyOtpView.as_view(), name="verify-otp"),
    path("/reset-password", ResetPasswordView.as_view(), name="reset-password"),
    path("/user-profile", UserProfileView.as_view(), name="user-profile"),
    path("/user-update", UserProfileUpdateView.as_view(), name="update-profile"),
    path("/logout", UserLogoutView.as_view(), name="user-logout")
]   