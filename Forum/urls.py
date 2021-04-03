from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from core.views import singup
from posts.views import frontpage, user_post, vote, details

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("post/<int:post_id>/", details, name="details"),
    path("post/<int:post_id>/vote", vote, name="vote"),
    path("post/", user_post, name="user_post"),
    path("signup/", singup, name="signup"),
    path(
        "login/", views.LoginView.as_view(template_name="core/login.html"), name="login"
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
    path("api/", include("API.urls")),
]
