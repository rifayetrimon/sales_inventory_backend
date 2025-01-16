import random
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.views import APIView
from . serializers import UserProfileSerializer, UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

User = get_user_model()



# User Registration 
class UserRegistrationView(APIView):
    def post(self, request):
        searializer = UserRegistrationSerializer(data=request.data)
        if searializer.is_valid():
            searializer.save()
            return Response({
                'status': "success",
                'message': 'User Created Successfully'
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': "error",
            'message': "User is already created"
        }, status=status.HTTP_400_BAD_REQUEST)
    

# User Login
class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)

        if user:

            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    'status': 'success',
                    'message': 'User Logged in Successfully',
                    'token': str(refresh.access_token)
                }, status=status.HTTP_200_OK
            )

        return Response({
            'status': 'unauthorized',
            'message': 'Invalid Credentials'
        }, status=status.HTTP_400_BAD_REQUEST)


# Send OTP
class sentOtpView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if not email or not User.objects.filter(email=email).exists():
            return Response({
                'status': 'error',
                'message': 'Valid email is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        otp = str(random.randint(100000, 999999))
        user = User.objects.get(email=email)
        user.otp = otp
        user.save()

        send_mail(
            subject='OTP for Password Reset',
            message=f'Your OTP is {otp}',
            from_email="Sales Inventory<rifayetrimon88@gmail.com>",
            recipient_list=[email],
        )
        return Response({
            'status': 'success',
            'message': 'OTP sent successfully'
        }, status=status.HTTP_200_OK)


# Verify OTP
class VerifyOtpView(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")

        if not email or not otp:
            return Response({
                'status': 'error',
                'message': 'Valid email and otp is required'}, 
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        try:
            user = User.objects.get(email=email, otp=otp)
            user.otp = None
            user.save()
            
            token = str(RefreshToken.for_user(user).access_token)
            return Response({
                'status': 'success',
                'message': 'OTP verified successfully',
                'token': token
            }, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Invalid OTP'
            }, status=status.HTTP_400_BAD_REQUEST)
        

# Reset Password

class ResetPasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        password = request.data.get("password")

        if not password:
            return Response({
                'status': 'error',
                'message': 'Password is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        user.set_password(password)
        user.save()

        return Response({
            'status': 'success',
            'message': 'Password reset successfully'
        }, status=status.HTTP_200_OK)
    


# User Profile

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = UserProfileSerializer(user).data


        return Response({
            'status': 'success',
            'message': 'Request successful',
            'data': user_data,
        }, status=status.HTTP_200_OK
        )
    



# user update 

class UserProfileUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user = request.user
        user_data = UserProfileSerializer(user, data=request.data, partial=True)

        if user_data.is_valid():
            user_data.save()
            return Response({
                'status': 'success',
                'message': 'User updated successfully'
            }, status=status.HTTP_200_OK)

        return Response({
            'status': 'error',
            'message': 'Invalid data'
        }, status=status.HTTP_400_BAD_REQUEST)
       
    

# logout 

class UserLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({
                'status': 'success',
                'message': 'User Logged out successfully'
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'status': 'error',
                'message': 'Invalid token'
            }, status=status.HTTP_400_BAD_REQUEST)
    