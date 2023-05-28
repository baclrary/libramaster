from rest_framework import viewsets
from authentication.models import CustomUser
from author.models import Author
from order.models import Order
from book.models import Book
from .serializers import AuthorSerializer, CustomUserSerializer, OrderSerializer,  BookSerializer

from rest_framework import generics
from rest_framework.exceptions import NotFound


class CustomUserOrderList(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Order.objects.filter(user_id=user_id)


class CustomUserOrderDetail(generics.RetrieveAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Order.objects.filter(user_id=user_id)

    def get_object(self):
        queryset = self.get_queryset()
        order_id = self.kwargs['order_id']
        try:
            return queryset.get(pk=order_id)
        except Order.DoesNotExist:
            raise NotFound(detail="Order not found for the given user")


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
