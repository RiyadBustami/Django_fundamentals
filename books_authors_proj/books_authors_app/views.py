from django.shortcuts import render,HttpResponse,redirect
from books_authors_app.models import Book,Author

# Create your views here.
def books_index(request):
    context={
        "books":Book.objects.all(),
        "authors":Author.objects.all(),
    }
    return render(request,"books_index.html",context)

def add_new_book(request):
    title=request.POST['title']
    desc=request.POST['desc']
    Book.objects.create(title=title,desc=desc)
    return redirect("/")

def books_show(request,id):
    book_authors=Book.objects.get(id=id).authors.all()
    authors=Author.objects.all()
    not_book_authors=[]
    for element in authors :
        if element not in book_authors:
            not_book_authors.append(element)
    context={
        "book":Book.objects.get(id=id),
        "book_authors":Book.objects.get(id=id).authors.all(),
        "not_book_authors":not_book_authors,        
    }
    return render(request,"books_show.html",context)

def add_author(request,id):
    book_id=id
    author_id=request.POST['author']
    Book.objects.get(id=book_id).authors.add(Author.objects.get(id=author_id))

    return redirect("/books/"+id)

def authors_index(request):
    context={
        "books":Book.objects.all(),
        "authors":Author.objects.all(),
    }
    return render(request,"authors_index.html",context)

def add_new_author(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    notes=request.POST['notes']
    Author.objects.create(first_name=first_name,last_name=last_name,notes=notes)
    return redirect("/authors")

def authors_show(request,id):
    author_books=Author.objects.get(id=id).books.all()
    books=Book.objects.all()
    not_author_books=[]
    for element in books :
        if element not in author_books:
            not_author_books.append(element)
    context={
        "author":Author.objects.get(id=id),
        "author_books":Author.objects.get(id=id).books.all(),
        "not_author_books":not_author_books,        
    }
    return render(request,"authors_show.html",context)

def add_book(request,id):
    author_id=id
    book_id=request.POST['book']
    Author.objects.get(id=author_id).books.add(Book.objects.get(id=book_id))

    return redirect("/authors/"+id)