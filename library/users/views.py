from django.shortcuts import render
from users.models import Users
# Create your views here.
def register(request):

    return render(request,'register.html',)
def login(request):
    context={'username':'Arun','password':'eg :- Arun@123'}
    return render(request,'login.html',context)
def logout(request):
    return login(request)

def viewusers(request):
    k = Users.objects.all()
    return render(request,'viewusers.html',{'users':k})