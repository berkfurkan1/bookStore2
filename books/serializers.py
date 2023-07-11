from rest_framework import serializers
 
from books.models import Author,Book

class BookStoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return Author.create(validated_data)
    
    def create(self, validated_data):
        return Book.create(validated_data)
    #create methodu post isteklerine karşılık gelecek ve Author , Book model sınıflarının varsayılan objects model manager referansını kullanıp doğrulanmış veriyi(validated data) oluşturacak.