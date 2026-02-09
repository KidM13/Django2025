from django.shortcuts import render

# Create your views here.
# FBV

from django.http import HttpResponse
from .models import Book

def list_books(request):
    books = Book.objects.select_related('author').prefetch_related('categories')

    output = ""
    for book in books:
        categories = ", ".join([c.name for c in book.categories.all()])
        output += f"{book.title} - {book.author.name} - {categories}<br>"

    return HttpResponse(output)

# CBV

from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book, Member, Loan
from django.utils import timezone

class AddLoanView(View):
    def post(self, request, book_id):
        member_id = request.POST.get('member_id')

        book = get_object_or_404(Book, id=book_id)
        member = get_object_or_404(Member, id=member_id)

        Loan.objects.create(
            book=book,
            member=member,
            loan_date=timezone.now()
        )

        return HttpResponse("Loan added successfully")

