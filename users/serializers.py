from rest_framework import serializers


from users.models import User


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "last_login", "email", "phone", "role", "is_active"]

class UsersCreateSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username",
                  "password", "last_login", "email", "phone",
                  "role", "is_active"]

    def is_valid(self, *, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

class UsersUpdateSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username",
                  "password", "last_login", "email", "phone",
                  "role", "is_active"]

    def is_valid(self, *, raise_exception=False):
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()
        user.save()
        return user


