from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import Users, CustomUser
from django.http import HttpResponse


# Create your views here.
def adminreg(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        a = request.POST['a']
        n = request.POST['n']
        if p == c:
            u = CustomUser.objects.create_user(username=u, password=p, first_name=f, last_name=l, email=e, address=a,
                                               phone=n, is_superuser=True)
            u.save()
        else:
            return HttpResponse("Passwords are not same")
        return redirect('users:user_login')
    return render(request, 'adminregister.html')


def userreg(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        a = request.POST['a']
        n = request.POST['n']
        if p == c:
            u = CustomUser.objects.create_user(username=u, password=p, first_name=f, last_name=l, email=e, address=a,
                                               phone=n, is_user=True)
            u.save()
        else:
            return HttpResponse("Passwords are not same")
        return redirect('users:user_login')
    return render(request, 'userregister.html')


def view_user(request):
    k = User.objects.all()
    return render(request, 'ViewUser.html', {'users': k})


def user_login(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('books:home')
        else:
            return HttpResponse("Invalid")
    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('users:user_login')
