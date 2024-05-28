from rest_framework import serializers
from blog import models


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['title', 'content', 'category', 'tags', 'image']

    def create(self, validated_data):
        tags = validated_data.pop('tags')

        post = models.Post.objects.create(**validated_data, author=self.context.get('request').user)
        for tag in tags:
            post.tags.add(tag)
        return post


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['content']
