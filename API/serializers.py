from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Posts, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
