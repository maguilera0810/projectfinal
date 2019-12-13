from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("registration/", views.registration, name="registration"),
    path("logout/", views.logout_view, name="logout"),
    path("videos/", views.video, name="videos"),
    path("comments/", views.AddComment, name="comments")
    
]
