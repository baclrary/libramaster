from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "orders"

urlpatterns = [
    path('', views.OrdersList.as_view(), name='orders'),
    path('create/', views.create_order, name='order-create'),
    path('create_order/<int:book_id>/', views.create_order, name='order-create-with-book-id'),
    path('<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('<int:pk>/close', views.close_order, name='order-close')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
