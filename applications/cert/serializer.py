from django.db.migrations import serializer
from applications.cert.models import User

class UserSerializer(serializer.ModelSerializer):
    class Meta:
        model = User
        field = "__all__"
