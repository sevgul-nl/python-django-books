from django.urls import path, include

from books.views import blist, bdetail

urlpatterns = [
    path('', blist, name='blist'),
    path('<int:pk>/', bdetail, name='bdetail'),
]
