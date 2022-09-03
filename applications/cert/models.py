from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """
    공통 모델
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("가입일"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=("마지막 접속일"))

    class Meta:
        abstract = True

class User(BaseModel):
    id = models.IntegerField(primary_key=True)
    is_admin = models.BooleanField()
    email = models.CharField(max_length=30)
    sex = models.BooleanField()
    age = models.IntegerField()
    phone = models.IntegerField()

    class Meta:
        db_table = "user"