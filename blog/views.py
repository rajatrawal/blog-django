from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Blog, Comment
from django.contrib import messages
from blog.templatestag import extras
# Create your views here.


def index(request):
    blogs = Blog.objects.all()
    params = {"blogs": blogs}
    return render(request, "blog/index.html", params)


def blogPost(request, id):
    blog = Blog.objects.filter(id=id)[0]
    blog.views=blog.views+1
    blog.save()

    comments = Comment.objects.filter(
        post=blog, parent=None).order_by("time_stamp")
    replies = Comment.objects.filter(post=blog).exclude(parent=None)
    comments = comments.reverse()
    reDict = {}
    for replay in replies:
        if replay.parent.id not in reDict.keys():
            reDict[replay.parent.id] = [replay]
        else:
            reDict[replay.parent.id].append(replay)
    params = {"blog": blog, "comments": comments, "replies": reDict}
    return render(request, "blog/blogPost.html", params)


def postComment(request):
    if request.method == "POST":
        user = request.user
        parentSn = request.POST.get("parentSno")
        comment = request.POST["comment"]
        post = request.POST.get("postId")

        postObj = Blog.objects.get(id=post)
        if parentSn == "":
            if len(comment) > 0:
                newComment = Comment(Comment=comment, user=user, post=postObj)
                newComment.save()
                messages.info(
                    request, 'Your Comment Has Been Added Successfuly')

            else:
                messages.error(request, "Cant't Add Empty Comment")

        else:
            if len(comment) > 0:
                parent = Comment.objects.get(id=parentSn)
                comment = Comment(Comment=comment, user=user,
                                post=postObj, parent=parent)
                comment.save()
                messages.info(request, 'Your Replay Has Been Added Successfuly')
            else:
                messages.error(request, "Cant't Add Empty Replay")

    return redirect("/blog/blogPost/"+post)
