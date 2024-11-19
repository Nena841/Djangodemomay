from django.shortcuts import render
from employee.models import Employee
# Create your views here.

def home(request):
    k=Employee.objects.all()
    return render(request,'home.html',{'employee':k})

def add(request):
    if(request.method=='POST'):
        e=request.POST['e']
        n= request.POST['n']
        a= request.POST['a']
        ad = request.POST['ad']
        m = request.POST['m']
        i = request.FILES.get('i')
        m=Employee.objects.create(empid=e,ename=n,age=a,address=ad,email=m,image=i)
        m.save()
        return home(request)
    return render(request,'add.html')

def details(request,i):
    k = Employee.objects.get(id=i)
    return render(request,'details.html',{'employee':k})

def edit(request,i):
    k = Employee.objects.get(id=i)
    if(request.method=="POST"):
        k.empid=request.POST['e']
        k.ename=request.POST['n']
        k.age=request.POST['a']
        k.address=request.POST['ad']
        k.email = request.POST['m']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.image=request.FILES.get('i')
            k.save()
        return home(request)
    return render(request,'edit.html',{'employee':k})


def delete(request,i):
    k=Employee.objects.get(id=i)
    k.delete()
    return home(request)