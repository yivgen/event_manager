from rest_framework import generics
from users.models import MyUser
from rest_framework.permissions import AllowAny
from users.serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer