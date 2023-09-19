#books/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/', views.add_book, name='add_book'),
    path('update/<int:id>/', views.update_book, name='update_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
]
