from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("search/", views.search, name="search"),
    path("signup/", views.handel_sign_up, name="signup"),
    path("login/", views.handel_login, name="login"),
    path("logout/", views.handel_logout, name="logout"),
]
