from django.contrib import admin
from blog import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(models.Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(models.Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(models.Comment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author')
