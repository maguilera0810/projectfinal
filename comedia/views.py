from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import models
import json
from random import randint
# Create your views here.


def ColorRandom():
    a = "0123456789ABCDEF"
    c = "#"
    for i in range(6):
        c += a[(randint(0, 250)*randint(0, 250)+randint(0, 500)) % 16]
    return c


def index(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    return redirect("/videos/")


def logout_view(request):
    logout(request)
    # return render(request, "orders/login.html", {"message": "Logged out."})
    return redirect("/login/")


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("videos"))
        else:
            context = {"message": False}
            print(context)
            return render(request, "orders/login.html", context=context)
    else:
        return render(request, "orders/login.html", {"message": True})


def registration(request):
    context = {
        "client": models.Client.objects.all(),
        "client2": User.objects.all()
    }
    if request.method == 'POST':
        user = User.objects.create_user(request.POST.get(
            'username'), request.POST.get('email'), request.POST.get('password'))
        user.first_name = request.POST.get('name')
        user.last_name = request.POST.get('lastname')
        user.save()
        print("------------------------")
        print(user.first_name)
        print(user.last_name)
        print("------------------------")

        post = models.Client()
        post.firstname = request.POST.get('name')
        post.lastname = request.POST.get('lastname')
        post.username = request.POST.get('username')
        post.password = request.POST.get('password')
        post.email = request.POST.get("email")
        post.save()

        # return render(request, "orders/register.html", context)
        return redirect("/login/")

    else:
        return render(request, "orders/register.html", context)


def video(request):
    if (request.user.get_username()):
        videos = models.Video.objects.all()
        lvideos = len(videos)
        rango = 10
        lgroups = lvideos//rango
        print(lgroups, "//////////////////////")
        if len(videos)/rango > lgroups:
            lgroups += 1
        inicio0 = 0
        fin0 = rango
        pag = 0
        if request.method == "POST":
            pag = int(request.POST["pagina"])

            print(pag, type(pag), "//////*****------")
        inicio = inicio0 + rango * pag
        if fin0 + rango * pag <= lvideos:
            fin = fin0 + rango * pag
        else:
            fin = lvideos
        videos = videos[inicio:fin]
        print(videos)
        context = {
            "videos": videos,
            "groups": [i for i in range(lgroups)]
        }
        print(context)
        return render(request, "orders/videos.html", context=context)
    else:
        return redirect("/login/")


def AddComment(request):

    if request.method == 'POST':

        username = request.user.get_username()
        comment = request.POST["comment"]
        rank = request.POST["rank"]

        c = models.Comment(
            user_id=username,
            rank=rank,
            comment=comment
        )
        c.save()

    comments = models.Comment.objects.all()
    colors = []
    for i in comments:
        colors.append(ColorRandom())
    context = {
        "Comments": zip(colors, comments)
    }

    return render(request, "orders/comment.html", context)
