#books/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def book_list(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json


@csrf_exempt
@require_POST
def delete_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully'}, status=200)
    except Book.DoesNotExist:
        return JsonResponse({'message': 'Book not found'}, status=404)

# 추가적으로 필요한 add_book, update_book 뷰 함수도 이곳에 정의할 수 있습니다.
