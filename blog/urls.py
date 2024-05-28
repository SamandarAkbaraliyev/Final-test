from django.urls import path
from blog import views

urlpatterns = [
    path("post/create/", views.PostCreateAPIView.as_view()),

    path("post/<int:post_id>/comment/", views.CommentCreateAPIView.as_view())
]
