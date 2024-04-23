from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import MyModel


@login_required(login_url='login')
def terulet(request):
    if request.method == "POST":
        a = request.POST.get("a")
        b = request.POST.get("b")
        if a and b:
            return render(request, "terulet.html", {"active" : "terulet", "result" : str(float(a) * float(b))})
    return render(request, "terulet.html", {"active" : "terulet"})

@login_required(login_url='login')
def rolunk(request):
    return render(request, "rolunk.html", {"active" : "rolunk"})

@login_required(login_url='login')
def feladat(request):
    return render(request, "feladat.html", {"active" : "feladat"})

@login_required(login_url='login')
def kapcsolat(request):
    return render(request, "kapcsolat.html", {"active" : "kapcsolat"})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(password, username)
        acc = authenticate(request=request, username=username, password=password)
        if acc is not None:
            login(request, acc)
            return redirect("home")
        else:
            return render(request, 'login.html', {'error_message': 'Nem jó a felhasználónév vagy a jelszó!'})

    return render(request, "login.html")


@login_required(login_url='login')
def home(request):
    if request.method == "POST":
        if "szamolas" in request.POST:
            a = request.POST.get("a")
            b = request.POST.get("b")
            try:
                if float(a) and float(b):
                    return render(request, "home.html", {"user" : request.user, "data" : MyModel.objects.all(), "active" : "home", "result" : str(float(a) * float(b))})
            except:
                return render(request, "home.html", {"user" : request.user, "data" : MyModel.objects.all(), "active" : "home"})
        elif "logout" in request.POST:
            logout(request)
            return redirect("login")
    return render(request, "home.html", {"user" : request.user, "active" : "home", "data" : MyModel.objects.all()})


def register(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            r_password = request.POST['repeate-password']
            if password != r_password:
                return render(request, 'register.html', {'error_message': 'A jelszavak nem egyeznek!'})

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error_message': 'A felhasználónév már foglalt!'})
            
            # Create the user
            user = User.objects.create_user(username=username, password=password)
            user.save()
            # Log in the user
            
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to home page or any other page
    else:
        return render(request, 'register.html')