from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from books.models import Book

context = {'name': 'Arun', 'age': 21}


# Create your views here.
def home(request):
    return render(request, 'home.html', context)


@login_required
def add_books(request):
    if request.method == "POST":
        t = request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        pr = request.POST['pr']
        l = request.POST['l']
        i = request.FILES['i']
        f = request.FILES['f']

        b = Book.objects.create(title=t, author=a, pages=p, price=pr, language=l, cover=i, pdf=f)
        b.save()  # saves the record inside table
        return redirect('books:view')
    return render(request, 'add.html')


@login_required
def view_books(request):
    # k=con.execute('select * from Book')
    k = Book.objects.all()  # Reads all records from table Book and assigns it to k
    return render(request, 'view.html', {'book': k})


@login_required
def detail(request, p):
    k = Book.objects.get(id=p)
    return render(request, 'detail.html', {'book': k})


@login_required
def edit(request, p):
    k = Book.objects.get(id=p)
    if request.method == "POST":
        k.title = request.POST['t']
        k.author = request.POST['a']
        k.pages = request.POST['p']
        k.price = request.POST['pr']
        k.language = request.POST['l']
        if request.FILES.get('i') == "None":
            k.save()
        else:
            k.cover = request.FILES.get('c')
        if request.FILES.get('f') == "None":
            k.save()
        else:
            k.pdf = request.FILES.get('f')
        k.save()
        return view_books(request)

    return render(request, 'edit.html', {'book': k})


@login_required
def delete(request, p):
    k = Book.objects.get(id=p)
    k.delete()
    return redirect('books:view')


def search(request):
    k = None  # initialize k as none
    if request.method == "POST":  # get the input key from form
        query = request.POST['q']
        print(query)
        if query:
            k = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
            # it checks the key in title and author field of every records.
            # filter() returns only the matching records.
    return render(request, 'search.html', {'book': k})
