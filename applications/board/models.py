from django.db import models

# Create your models here.
from applications.cert.models import BaseModel, User

class BaseBoard(BaseModel):
    """
    게시판 공통 모델 - User의 BaseModel 상속 받고 있음
    """
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=300, verbose_name="제목")
    contents = models.CharField(max_length=300, verbose_name="내용")

class NoticeBoard(BaseBoard):
    """
    공지 사항
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("user_id"))

    class Meta:
        db_table = "notice"

class FreeBoard(BaseBoard):
    """
    자유 게시판
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("user_id"))

    class Meta:
        db_table = "free"

class Operation(BaseBoard):
    """
    운영 게시판
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("user_id"))

    class Meta:
        db_table = "operation"