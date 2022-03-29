from django.db import models


class Book(models.Model):
    authors = models.ManyToManyField('Person')
    language = models.CharField(max_length=16, null=True)
    title = models.CharField(blank=True, max_length=1024, null=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return str(self.id)


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
