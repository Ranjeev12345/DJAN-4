from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Book

def home(request):
    books = Book.objects.all()  # start with all books

    # Filter parameters from GET request
    name = request.GET.get("name")
    author = request.GET.get("author")
    genre = request.GET.get("genre")
    year = request.GET.get("year")
    search = request.GET.get("search")  # new search box

    if name:
        books = books.filter(name__icontains=name)
    if author:
        books = books.filter(author__icontains=author)
    if genre:
        books = books.filter(genre__icontains=genre)
    if year:
        try:
            books = books.filter(year_published=int(year))
        except ValueError:
            pass  # ignore invalid year input

    if search:
        books = books.filter(
            Q(name__icontains=search) |
            Q(author__icontains=search) |
            Q(genre__icontains=search)
        )

    # Sorting parameter
    sort_by = request.GET.get("sort_by")
    if sort_by in ['name', '-name', 'author', '-author', 'genre', '-genre', 'year_published', '-year_published']:
        books = books.order_by(sort_by)

    return render(request, "main.html", {"books": books})

def add_book(request):
    if request.method == "POST":
        name = request.POST.get("name")
        author = request.POST.get("author")
        genre = request.POST.get("genre")
        year_published = request.POST.get("year_published")
        if name and author and genre and year_published:
            Book.objects.create(
                name=name,
                author=author,
                genre=genre,
                year_published=int(year_published)
            )
            return redirect("/")
    return render(request, "add_book.html")

def delete_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        Book.objects.filter(id=book_id).delete()
        return redirect("/")
    books = Book.objects.only("id", "name", "author")
    return render(request, "delete_book.html", {"books": books})
