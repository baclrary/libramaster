from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path('', views.BooksList.as_view(), name='books'),
    path('<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('create/', views.create_book, name='book-create'),
]
