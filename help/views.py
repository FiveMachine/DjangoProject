from django.shortcuts import render

# Create your views here.


def help(request):
    return render(request, "help.html")
