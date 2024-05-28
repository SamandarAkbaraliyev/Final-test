from django.db import models
from utils.models import BaseModel
from ckeditor.fields import RichTextField


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Tag(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='posts')

    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    content = RichTextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


