from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db import IntegrityError

# Create your views here.


def signupaccount(request):
    if request.method == "GET":
        return render(request, "signupaccount.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(
                    request,
                    "signupaccount.html",
                    {
                        "form": UserCreationForm,
                        "error": "Username already taken. Choose new username.",
                    },
                )
        else:
            return render(
                request,
                "signupaccount.html",
                {"form": UserCreationForm, "error": "Passwords do not match."},
            )

@login_required
def logoutaccount(request):
    logout(request)
    return redirect("home")

def loginaccount(request):
    if request.method == 'GET':
        return render(request , 'loginaccount.html' , {'form' : AuthenticationForm})
    else:
        user = authenticate(request , username = request.POST['username'] , password = request.POST['password'])
        if user is None:
            return render(request , 'loginaccount.html' , {'form':AuthenticationForm , 'error': 'username and password do not match.'})
        else:
            login(request , user)
            return redirect("home")