from django.contrib import messages  # Import the messages module
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from authentication.forms import RegistrationForm


def home(req):
    return render(
        req,
        "index.html",
    )


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Logged In Successfully")
                return redirect(
                    "home"
                )  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def user_logout(request):
    username = request.user.username
    logout(request)
    messages.warning(request, f"Logged Out Successfully")
    return redirect("home")  # Redirect to the home page after successful logout


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(password)
            messages.success(
                request,
                f"Your account has been created successfully. Please log in.",
            )
            return redirect(
                "login"
            )  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()

    return render(request, "signup.html", {"form": form})
