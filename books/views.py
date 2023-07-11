from django.shortcuts import render
from django.http import HttpResponse # kullanıcıdan istek alıp cevap verebilmeyi sağlar.
from django.template  import loader
from .models import Author # from books.models import Author, Book
from .models import Book
from django.http import Http404
from django.http import JsonResponse
# Create your views here.
##############################
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# dahili importlar
from books.serializers import BookStoreSerializer


class BookList(APIView):#BookList sınıfı APIView sınıfını miras alıyor.
    def get(self,request,format=None):#Url üzerinden bu sınıfa yapılacak GET request(istek)leri bu method karşılayacak.
        books = Book.objects.all()#Django sorgusu ile bütün kayıtlı dataları veritabanından alıyoruz.
        seralizer = BookStoreSerializer(books,many=True)#diyerek veritabanından alınan bütün datayı serialize ediyoruz. Yani Book sınıfına ait nesneyi kolayca ulaşılabilir bir formata çeviriyoruz.
        return Response(seralizer.data)#cevap olarak da uygun formata çevrilmiş datayı cevap olarak dönüyoruz.
    
    def post(self,request, format= None):#bizim için şu anlık önemli olan request parametresi. Client'ın yaptığı isteğe dair veriyi, bilgileri request taşıyacaktır.
        serializer = BookStoreSerializer(data=request.data)#diyerek serializer sınıfımıza client'ın gönderdiği veriyi gönderiyoruz.
        #request.data içerisinde client'ın yaptığı post methodu ile gönderilen data bulunuyor.
        if serializer.is_valid():#diyerek gelen datanın uygun formatta olup olmadığını kontrol ediyoruz.
            serializer.save()#format uygunsa kaydetme işlemi
            return Response(serializer.data,status=status.HTTP_201_CREATED)#cevap olarak kaydedilen data ve HTTP cevap mesajı ve kodu.
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)#diyerek hata mesajlarını ve http mesajı ve kodunu cevap olarak veriyoruz.

def index(request):
    return HttpResponse("Anasayfa")

def authors(request):
   # template = loader.get_template('authors.html')
    context={
        'authors_list': Author.objects.all()

    }
    return render(request,'authors.html',context)

def books(request):
    #return HttpResponse("Kitaplar")
    context={
        'books_list': Book.objects.all()

    }
    return render(request,'books.html',context)

def bookDetails(request,bookId):
    try:
        context={
        'book_detail': Book.objects.get(pk=bookId)

    }
    except Book.DoesNotExist:
        raise Http404("Yazar bulunamadi")

    return render(request,'bookDetail.html',context)

def chooseAbook(request):
    return HttpResponse("url'in devamina kitap id'si giriniz")




#API
