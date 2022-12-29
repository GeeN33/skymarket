from django.core.exceptions import ValidationError
from rest_framework import serializers

from ads.models import Ad, Comment
from users.models import User



class AdCreateSerializers(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    author = serializers.SlugRelatedField(queryset=User.objects.all(),   slug_field="first_name",  required=False)

    class Meta:
        model = Ad
        fields = ["id", "title", "author","price","image","created_at"]

    def is_valid(self, *, raise_exception=False):
        self._author = self.initial_data.pop("author")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)
        try:
            ad.author = User.objects.get(id=self._author)
        except User.DoesNotExist:
            raise ValidationError("Users not")

        ad.save()
        return ad

class AdListSerializers(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(queryset=User.objects.all(),   slug_field="first_name",  required=False)

    class Meta:
        model = Ad
        fields = ["id", "title", "author","price","image","created_at"]

class AdDetaiSerializers(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(queryset=User.objects.all(),   slug_field="first_name",  required=False)

    class Meta:
        model = Ad
        fields = ["id", "title", "author","price","image","created_at"]

class AdUpdateSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="first_name", required=False)

    class Meta:
        model = Ad
        fields = ["id", "title", "author", "price", "image", "created_at"]

    def is_valid(self, *, raise_exception=False):
        self._author = self.initial_data.pop("author")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        ad = super().save()
        try:
            ad.author = User.objects.get(id=self._author)
        except User.DoesNotExist:
            raise ValidationError("Users not")
        ad.save()
        return ad

class AdDestroySerializers(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]


class CommentCreateSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    author = serializers.SlugRelatedField(queryset=User.objects.all(),   slug_field="first_name",  required=False)
    ad = serializers.SlugRelatedField(queryset=Ad.objects.all(), slug_field="id", required=False)

    class Meta:
        model = Comment
        fields = ["id", "text", "author","ad","created_at"]

    def is_valid(self, *, raise_exception=False):
        self._author = self.initial_data.pop("author")
        self._ad = self.initial_data.pop("ad")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        com = Comment.objects.create(**validated_data)
        try:
            com.author = User.objects.get(id=self._author)
        except User.DoesNotExist:
            raise ValidationError("Users not")
        try:
              com.ad = Ad.objects.get(id=self._ad)
        except Comment.DoesNotExist:
            raise ValidationError("Ads not")


        com.save()
        return com

class CommenListtSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    author = serializers.SlugRelatedField(queryset=User.objects.all(),   slug_field="first_name",  required=False)
    ad = serializers.SlugRelatedField(queryset=Ad.objects.all(), slug_field="id", required=False)

    class Meta:
        model = Comment
        fields = ["id", "text", "author","ad","created_at"]

class CommenUpdateSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="first_name", required=False)
    ad = serializers.SlugRelatedField(queryset=Ad.objects.all(), slug_field="id", required=False)

    class Meta:
        model = Comment
        fields = ["id", "text", "author", "ad", "created_at"]


    def is_valid(self, *, raise_exception=False):
        self._author = self.initial_data.pop("author")
        self._ad = self.initial_data.pop("ad")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        com = super().save()
        try:
            com.author = User.objects.get(id=self._author)
        except User.DoesNotExist:
            raise ValidationError("Users not")
        try:
            com.ad = Ad.objects.get(id=self._ad)
        except Comment.DoesNotExist:
            raise ValidationError("Ads not")

        com.save()
        return com

class CommentDestroySerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id"]
