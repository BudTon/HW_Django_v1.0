from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    print(books)
    context = {'books': books}
    return render(request, template, context)

def book(request):
    list_pagi_book = Book.objects.all()
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(list_pagi_book, 1)
    page = paginator.get_page(page_number)
    context = {
        'books': page.object_list,
        'page': page,
    }
    return render(request, 'books/books_list.html', context)

