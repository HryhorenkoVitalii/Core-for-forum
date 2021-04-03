from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from posts.models import Posts, Comment
from .serializers import UserSerializer, PostsSerializer, CommentSerializer


class ApiUserViews(viewsets.ViewSet):

    def get_all_users(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)

    def get_user(self, request, pk):
        data = User.objects.get(id=pk)
        serializer = UserSerializer(data, many=False)
        return Response(serializer.data)

    def create_user(self, request):
        data = request.data
        data["password"] = make_password(data["password"])
        serializer = UserSerializer(data=data, many=False)

        if serializer.is_valid():

            serializer.save()

        return Response(serializer.data)

    def update_user(self, request, pk):
        data = User.objects.get(id=pk)
        serializer = UserSerializer(instance=data, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def delete_user(self, request, pk):
        data = User.objects.get(id=pk)
        data.delete()
        return Response({"detail": f"User id={pk} is deleted"})


class ApiPostsViews(viewsets.ViewSet):
    def get_all_posts(self, request):
        data = Posts.objects.all()
        serializer = PostsSerializer(data, many=True)
        return Response(serializer.data)

    def get_post(self, request, pk):
        data = Posts.objects.get(id=pk)
        serializer = PostsSerializer(data, many=False)
        return Response(serializer.data)

    def create_post(self, request):
        data = request.data
        serializer = PostsSerializer(data=data, many=False)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def update_post(self, request, pk):
        data = Posts.objects.get(id=pk)
        serializer = PostsSerializer(instance=data, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def delete_post(self, request, pk):
        data = Posts.objects.get(id=pk)
        data.delete()
        return Response({"detail": f"Post id={pk} is deleted"})


class ApiCommentsViews(viewsets.ViewSet):
    def get_all_comments(self, request):
        data = Comment.objects.all()
        serializer = CommentSerializer(data, many=True)
        return Response(serializer.data)

    def get_comment(self, request, pk):
        data = Comment.objects.get(id=pk)
        serializer = CommentSerializer(data, many=False)
        return Response(serializer.data)

    def comment_create(self, request):
        data = request.data
        serializer = CommentSerializer(data=data, many=False)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def comment_update(self, request, pk):
        data = Comment.objects.get(id=pk)
        serializer = CommentSerializer(instance=data, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def comment_delete(self, request, pk):
        data = Comment.objects.get(id=pk)
        data.delete()
        return Response({"detail": f"Comment id={pk} is deleted"})
