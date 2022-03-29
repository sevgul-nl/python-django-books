from .models import Book, Review, Person
from .utils import arating
from django.shortcuts import render, get_object_or_404


def blist(request):
    db_books = Book.objects.all().prefetch_related('authors')
    books = []
    for book in db_books:
        reviews = book.review_set.all()
        if reviews:
            brating = arating([review.rating for review in reviews])
            nreviews = len(reviews)
        else:
            brating = None
            nreviews = 0
        books.append({'book': book, 'book_rating': brating, \
                      'number_of_reviews': nreviews, 'authors': book.authors.all()})
    context = {
        "list": books
    }
    return render(request, "blist.html", context)


def bdetail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        brating = arating([review.rating for review in reviews])
        context = {
            "book": book,
            "authors": book.authors.all(),
            "book_rating": brating,
            "reviews": reviews
        }
    else:
        context = {
            "book": book,
            "authors": book.authors.all(),
            "book_rating": None,
            "reviews": None
        }
    return render(request, "bdetail.html", context)
