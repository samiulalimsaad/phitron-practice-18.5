from django.shortcuts import redirect, render


def index(req):
    return render(req, "index.html")


def login(req):
    return render(req, "login.html")


def logout(req):
    return redirect("login")


def signup(req):
    return render(req, "signup.html")
