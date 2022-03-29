from books.models import Book, Person


def data():
    book = Book.objects.create(title='Condensed History of the ßMexican War and its Glorious Results', language='en')