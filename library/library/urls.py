"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import home_page, UserDetail, UserList
from rest_framework.routers import DefaultRouter
from . import viewsets


router = DefaultRouter()
router.register(r'user', viewsets.CustomUserViewSet, basename='user')
router.register(r'author', viewsets.AuthorViewSet, basename='author')
router.register(r'order', viewsets.OrderViewSet, basename='order')
router.register(r'book', viewsets.BookViewSet, basename='book')



urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("books/", include("book.urls")),
    path('users/', UserList.as_view(), name='users'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('authors/', include("author.urls")),
    path("orders/", include("order.urls")),
    path('api/v1/', include(router.urls)),
    path('api/v1/user/<int:user_id>/order/', viewsets.CustomUserOrderList.as_view(), name='user-orders'),
    path('api/v1/user/<int:user_id>/order/<int:order_id>/', viewsets.CustomUserOrderDetail.as_view(), name='user-order-detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
