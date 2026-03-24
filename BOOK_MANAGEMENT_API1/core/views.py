from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Author


from .models import Book


def get_books(request):
    books = Book.objects.select_related('author').all()

    data = []
    for book in books:
        data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author.name,
            "price": str(book.price),
            "available": book.available,
        })

    return JsonResponse(data, safe=False)