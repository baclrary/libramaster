from django.urls import path

from . import views

app_name = "author"

urlpatterns = [
    path('', views.AuthorsList.as_view(), name='authors'),
    path('<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('create/', views.create_author, name='author-create'),
    path('<int:pk>/delete/', views.delete_author, name='author-delete'),
]
