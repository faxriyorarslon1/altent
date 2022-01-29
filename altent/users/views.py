from django.utils.translation import ugettext_lazy as _
# from django_rest_resetpassword.signals import reset_password_token_created
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
from .serializers import (CustomTokenObtainPairSerializer,
                          UserSerializer)

# Create your views here.

class UsersRegisterView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if 'password' in request.data:
            if serializer.is_valid():
                password = request.data["password"]
                if len(password) < 8:
                    return Response(
                        {"detail": _(
                            "Password length should not be less than 8 characters.")},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                serializer.save()
                user = User.objects.get(username=serializer.data['username'])
                refresh_token = RefreshToken().for_user(user)
                access_token = str(RefreshToken().for_user(user).access_token)
                refresh_token = str(refresh_token.access_token)
                response_data = {'access': access_token,
                                 'refresh': refresh_token}
                response_data.update(serializer.data)
                return Response(response_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(
                {"detail": _("Password field is required.")},
                status=status.HTTP_400_BAD_REQUEST
            )

class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class = CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()