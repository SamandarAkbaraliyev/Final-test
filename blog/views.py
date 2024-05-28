from django.shortcuts import render
from blog.models import Post, Comment
from blog import serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostCreateSerializer
    permission_classes = (IsAuthenticated,)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentCreateSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        
        comment = Comment

