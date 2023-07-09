from django.shortcuts import render
from django.http import HttpResponse # kullanıcıdan istek alıp cevap verebilmeyi sağlar.
from django.template  import loader
from .models import Author
from .models import Book
from django.http import Http404
# Create your views here.
##############################
#from rest_framework.views import APIView
#from rest_framework.response import Response


#class HelloApiView(APIView):
#    """Test API View."""
#    def get(self,request,format=None):
#        """Returns a list of APIView features."""

#        an_apiview=[
#            'Uses HTTP methods as function (get,post,patch,put,delete)',
 #           'It is similar to a traditional Django view',
  #          'Gives you the most control over your logic',
   #         'Is mapped manually to URLs'
    #    ]

     #   return Response({'message':'Hello!','an_apiview':an_apiview})



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
        raise Http404("Yazar bulunamadı")

    return render(request,'bookDetail.html',context)

def chooseAbook(request):
    return HttpResponse("url'in devamına kitap id'si giriniz")




