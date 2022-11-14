from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserLoginSerializer, UserRegisterSerializer
from django.contrib.auth.models import User


@api_view(['POST'])
def register_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(
        username=serializer.validated_data.get('username'),
        password=serializer.validated_data.get('password')
    )
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_view(request):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return Response(status=status.HTTP_403_FORBIDDEN,
                        data={'message': 'User data are wrong'})
    else:
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
        return Response(data={'key': token.key})