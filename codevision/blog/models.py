from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils.timezone import now


class Post(models.Model):
    sn = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=200)
    category = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    authorImage = models.ImageField(upload_to='media/blog/authorImages/')
    postImage = models.ImageField(upload_to='media/blog/postImages/')
    authorQuote = models.CharField(max_length=150)
    authorLink = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    seoTitle = models.CharField(max_length=200)
    content = models.TextField(max_length=20000)
    timeStamp = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class PostComments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    parent = models.ForeignKey('self', on_delete=CASCADE, null=True)
    time = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return "cmt by: "+self.user.username + " and comment is ' " + self.comment +" '"