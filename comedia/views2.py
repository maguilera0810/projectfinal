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
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "orders/menu.html", context)


def logout_view(request):
    logout(request)
    # return render(request, "orders/login.html", {"message": "Logged out."})
    return redirect("/login/")


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        print(username)
        password = request.POST["password"]
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "orders/login.html", {"message": "Ingresar porfa"})


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

        return render(request, "orders/register.html", context)

    else:
        return render(request, "orders/register.html", context)


def video(request):
    if (request.user.get_username()):
        context = {
            "regular_pizza": zip(models.Pizza.objects.filter(tipe="RP", size="S"), models.Pizza.objects.filter(tipe="RP", size="L")),
            "sicilian_pizza": zip(models.Pizza.objects.filter(tipe="SP", size="S"), models.Pizza.objects.filter(tipe="SP", size="L")),
            "toppings": models.Topping.objects.all(),
            "subs": zip(models.Pizza.objects.filter(tipe="Sub", size="S"), models.Pizza.objects.filter(tipe="Sub", size="L")),
            "pasta": models.Pizza.objects.filter(tipe="Pasta"),
            "salad": models.Pizza.objects.filter(tipe="Salad"),
            "dinnerplatters": zip(models.Pizza.objects.filter(tipe="DP", size="S"), models.Pizza.objects.filter(tipe="DP", size="L"))
        }

        return render(request, "orders/menu.html", context)
    else:
        return redirect("/login/")


def AddComment(request):

    if request.method == 'POST':

        username = request.user.get_username()
        comment = request.POST["comment"]
        rank = request.POST["rank"]
        c = models.Comment(
            userID=username,
            comment=comment,
            rank=rank
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
