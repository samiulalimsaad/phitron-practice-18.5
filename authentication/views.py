from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import redirect, render

from authentication.forms import ChangePasswordForm, RegistrationForm


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(
                request, user
            )  # Update the session to avoid logout
            messages.success(request, "Your password was successfully updated!")
            return redirect(
                "home"
            )  # Redirect to the home page after successful password change
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "change_password.html", {"form": form})


@login_required(login_url="/login/")
def change_password_without_old_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect("home")
    else:
        form = ChangePasswordForm(request.user)

    return render(request, "change_password_without_old_password.html", {"form": form})
