#books/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # @action(detail=False, methods=['POST'])
    # def add_book(self, request):
    #     serializer = BookSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status': 'Book added'}, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['POST'])
    # def update_book(self, request, pk=None):
    #     book = self.get_object()
    #     serializer = BookSerializer(book, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status': 'Book updated'}, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['POST'])
    # def delete_book(self, request, pk=None):
    #     book = self.get_object()
    #     book.delete()
    #     return Response({'status': 'Book deleted'}, status=status.HTTP_200_OK)


from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

#create
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        new_book = Book(title=title, author=author, price=price)
        new_book.save()

        return JsonResponse({'status': 'Book added'})

#read
def book_list(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

#update
def update_book(request, id):
    if request.method == 'POST':
        book = Book.objects.get(pk=id)

        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        book.title = title
        book.author = author
        book.price = price
        book.save()

        return JsonResponse({'status': 'Book updated'})

#delete
def delete_book(request, id):
    if request.method == 'POST':
        book = Book.objects.get(pk=id)
        book.delete()
        return JsonResponse({'status': 'Book deleted'})

