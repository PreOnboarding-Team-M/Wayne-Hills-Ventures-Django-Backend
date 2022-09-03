from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins

from applications.board.models import NoticeBoard, FreeBoard
from applications.board.serializer import NoticeSerializer, FreeSerializer


class NoticeMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    공지 사항 생성 및 조회
    """
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)

class NoticeDetailMixins(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    """
    수정 및 삭제
    """
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class FreeMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    자유 게시판 게시글 생성 및 조회
    """
    queryset = FreeBoard.objects.all()
    serializer_class = FreeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)

class FreeDetailMixins(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    """
    자유 게시판 게시글 수정 및 삭제
    """
    queryset = FreeBoard.objects.all()
    serializer_class = FreeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class OperationMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    운영 게시판 게시글 생성 및 조회
    """
    queryset = FreeBoard.objects.all()
    serializer_class = FreeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)

class OperationDetailMixins(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    """
    운영 게시판 게시글 수정 및 삭제
    """
    queryset = FreeBoard.objects.all()
    serializer_class = FreeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)