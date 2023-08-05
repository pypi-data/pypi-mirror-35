from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False, read_only=True)
    password = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email',)


# noinspection PyAbstractClass
class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)


# noinspection PyAbstractClass
class ResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


# noinspection PyAbstractClass
class ConfirmSerializer(serializers.Serializer):
    reset_token = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


# noinspection PyAbstractClass
class RefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(required=True)
