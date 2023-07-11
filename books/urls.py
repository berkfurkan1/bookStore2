#bu dosyayı biz oluşturuyoruz.
from django.urls import path
from . import views

from .views import BookList
urlpatterns=[
    path('',views.index,name='index'),
    path('books',views.books,name ='books'),
    path('authors',views.authors,name='authors'),
    path('bookdetail',views.chooseAbook,name='bookdetailERROR'),
    path('bookdetail/<int:bookId>',views.bookDetails,name='bookdetail'),
    #url(r'hello-view/',views.HelloApiView.as_view()),
    path('booklist/',BookList.as_view())#BookList.as_view() sınıfı view olarak dönüştürüp url'ye gelen isteklere cevap verecek hale getirir.
]