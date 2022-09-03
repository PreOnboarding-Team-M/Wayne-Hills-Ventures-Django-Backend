from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.generics import CreateAPIView

from applications.cert.models import User
from applications.cert.serializer import UserSerializer


class UserMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    회원 가입 및 회원 조회
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)

class UserDetailMixins(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    회원 정보 수정 및 탈퇴
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)