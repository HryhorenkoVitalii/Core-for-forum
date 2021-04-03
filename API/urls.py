from django.urls import path
from .views import ApiUserViews, ApiPostsViews, ApiCommentsViews

urlpatterns = [
    path(
        "v1/user/",
        ApiUserViews.as_view({"get": "get_all_users", "post": "create_user"}),
    ),
    path(
        "v1/user/<int:pk>",
        ApiUserViews.as_view(
            {"get": "get_user", "put": "update_user", "delete": "delete_user"}
        ),
    ),
    path(
        "v1/post/",
        ApiPostsViews.as_view({"get": "get_all_posts", "post": "create_post"}),
    ),
    path(
        "v1/post/<int:pk>",
        ApiPostsViews.as_view(
            {"get": "get_post", "put": "update_post", "delete": "delete_post"}
        ),
    ),
    path(
        "v1/comment/",
        ApiCommentsViews.as_view({"get": "get_all_comments", "post": "comment_create"}),
    ),
    path(
        "v1/comment/<int:pk>",
        ApiCommentsViews.as_view(
            {"get": "get_comment", "put": "post_comment", "delete": "delete_comment"}
        ),
    ),
]
