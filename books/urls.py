#bu dosyayı biz oluşturuyoruz.
from django.urls import path
from . import views
#from django.conf.urls import url
urlpatterns=[
    path('',views.index,name='index'),
    path('books',views.books,name ='books'),
    path('authors',views.authors,name='authors'),
    path('bookdetail',views.chooseAbook,name='bookdetailERROR'),
    path('bookdetail/<int:bookId>',views.bookDetails,name='bookdetail'),
    #url(r'hello-view/',views.HelloApiView.as_view()),
]