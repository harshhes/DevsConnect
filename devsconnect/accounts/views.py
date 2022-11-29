from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

def home(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
        print(user)
    except User.DoesNotExist:
        return None
    if user.check_password(password):
        return user

class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, format=None):

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email') 
            password = serializer.data.get('password') 

            user = authenticate_user(email=email, password=password)
            
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'msg': 'Login Successfully', "user_token": token}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non-field errors':{'email or password is not valid!!'}}}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
