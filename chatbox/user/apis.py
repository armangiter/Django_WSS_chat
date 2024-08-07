from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, CreateUserSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            self.permission_classes = [permissions.AllowAny, ]
            self.serializer_class = CreateUserSerializers
        return super().dispatch(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        serilized_data = CreateUserSerializers(data=request.data)
        if serilized_data.is_valid(raise_exception=True):
            user = User.objects.create(username=serilized_data.data["username"], email=serilized_data.data["email"])
            user.set_password(serilized_data.data['password'])
            user.save()
        return Response(data=serilized_data.data, status=201)

