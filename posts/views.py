from apscheduler.schedulers.blocking import BlockingScheduler
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostsForm, CommentForm
from .models import Posts, Vote


sched = BlockingScheduler()


def frontpage(request):
    posts = Posts.objects.all
    return render(request, "posts/frontpage.html", {"posts": posts})


def details(request, post_id):
    user_post = get_object_or_404(Posts, pk=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = user_post
            comment.author_name = request.user

            comment.save()

            return redirect("details", post_id=post_id)
    else:
        form = CommentForm()

    return render(request, "posts/detail.html", {"user_post": user_post, "form": form})


@login_required
def user_post(request):
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            user_post = form.save(commit=False)
            user_post.author_name = request.user
            user_post.save()

            return redirect("frontpage")
    else:
        form = PostsForm()
    return render(request, "posts/post.html", {"form": form})


@login_required
def vote(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)

    if post.author_name != request.user:
        Vote.objects.create(post=post, author_name=request.user)

    return redirect("frontpage")
