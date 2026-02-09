from django.urls import path
from .views import list_books, AddLoanView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/<int:book_id>/loan/', AddLoanView.as_view(), name='add_loan'),
]
