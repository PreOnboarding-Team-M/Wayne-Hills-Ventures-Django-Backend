from django.db.migrations import serializer

from applications.board.models import NoticeBoard, FreeBoard, Operation


class NoticeSerializer(serializer.ModelSerializer):
    class Meta:
        model = NoticeBoard
        field = "__all__"

class FreeSerializer(serializer.ModelSerializer):
    class Meta:
        model = FreeBoard
        field = "__all__"

class OperationSerializer(serializer.ModelSerializer):
    class Meta:
        model = Operation
        field = "__all__"