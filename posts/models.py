from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    posts = models.ForeignKey(
        Posts, related_name="votes_posts", on_delete=models.CASCADE
    )

    author_name = models.ForeignKey(
        User, related_name="votes_posts", on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        self.posts.amount_of_upvotes = self.posts.amount_of_upvotes + 1
        self.posts.save()

        super(Vote, self).save(*args, **kwargs)


class Comment(models.Model):

    post = models.ForeignKey(Posts, related_name="comments", on_delete=models.CASCADE)

    body = models.TextField()

    author_name = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creation_date"]
