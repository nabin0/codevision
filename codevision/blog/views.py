from typing import Pattern
from django import http
from django.db import connection
from django.shortcuts import redirect, render, HttpResponse
from django.db.models import Q
from .models import Post, PostComments
from django.contrib import messages
from blog.templatetags import extras


def blogHome(request):
    posts = Post.objects.all()
    params = {"posts": posts}
    return render(request, "blog/bloghome.html", params)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    if post is not None:
        category = post.category
    else:
        category = "General"
    posts = Post.objects.filter(~Q(slug=slug), category=category)
    comments = PostComments.objects.filter(post=post, parent=None)
    replies = PostComments.objects.filter(post=post).exclude(parent=None)
    replyDict ={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    print(post)
    contex = {"post": post, "posts": posts, "comments": comments, "replyDict":replyDict}
    return render(request, "blog/blogpost.html", contex)


def postComments(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = Post.objects.get(sn=postSno)

        if parentSno == "":
            if len(comment) > 0 and comment != " ":
                comment = PostComments(comment=comment, user=user, post=post)
                comment.save()
        else:
            if len(comment) > 0 and comment != " ":
                parent = PostComments.objects.get(sno=parentSno)
                comment = PostComments(
                comment=comment, user=user, post=post, parent=parent)
                comment.save()
                
    return redirect(f'/blog/{post.slug}')
