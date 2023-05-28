from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage, default_storage
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from .models import Book
from author.models import Author
from django.db.models import Q
from django.contrib import messages
from .forms import BookForm

class BooksList(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = "books/books_list.html"

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if query:
            query_parts = list(filter(None, query.split(' ')))

            if len(query_parts) == 3:
                # When there are three parts in the query: full name (first name, patronymic, and surname)
                books = Book.objects.filter(
                    Q(authors__name__icontains=query_parts[0]) &
                    Q(authors__patronymic__icontains=query_parts[1]) &
                    Q(authors__surname__icontains=query_parts[2])
                ).distinct()
            elif len(query_parts) == 2:
                # When there are two parts in the query: first name and surname
                books = Book.objects.filter(
                    Q(authors__name__icontains=query_parts[0]) &
                    Q(authors__surname__icontains=query_parts[1])
                ).distinct()
            else:
                # Handle the query for other cases
                books = Book.objects.filter(
                    Q(name__icontains=query) |
                    Q(authors__name__icontains=query) |
                    Q(authors__patronymic__icontains=query) |
                    Q(authors__surname__icontains=query) |
                    Q(description__icontains=query) |
                    Q(count__icontains=query)
                ).distinct()

            if not books:
                messages.error(self.request, "No book found")
            return books
        else:
            return Book.get_all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id_query = self.request.GET.get('user_id', '')

        if user_id_query:
            CustomUser = get_user_model()
            try:
                user = CustomUser.objects.get(pk=int(user_id_query))
                context['user_books'] = user.get_books()
                context['user_full_name'] = user.get_full_name()
            except CustomUser.DoesNotExist:
                context['user_books'] = []
                messages.error(self.request, f"There's no user with id {int(user_id_query)}")

        return context


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def post(self, request, *args, **kwargs):
        if "order_book" in request.POST:
            book_id = self.get_object().id
            return redirect(reverse('orders:order-create-with-book-id', args=(book_id,)))
        return super().post(request, *args, **kwargs)


def create_book(request):

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)

            title = form.cleaned_data['name']
            description = form.cleaned_data['description']
            count = form.cleaned_data['author_ids']
            author_ids_str = form.cleaned_data['author_ids']

            author_ids = [int(aid.strip()) for aid in author_ids_str.split(',') if aid.strip()]
            authors = Author.objects.filter(id__in=author_ids)

            if len(authors) != len(author_ids):
                for author_id in author_ids:
                    if not Author.objects.filter(id=author_id).exists():
                        messages.error(request, f"No author with id {author_id}")
                return render(request, 'books/book_create.html', {'form': form})

            if not authors:
                messages.error(request, "Provide authors")
                return render(request, 'books/book_create.html', {'form': form})

            if 'cover_image' in request.FILES:
                cover_image = request.FILES['cover_image']
                book = Book(name=title, description=description, count=count, cover_image=cover_image)
            else:
                book = Book(name=title, description=description, count=count)

            book.save()
            book.authors.set(authors)
            book.save()

            messages.success(request, "Book created successfully.")
            return redirect('books:books')

    else:
        form = BookForm()

    return render(request, 'books/book_create.html', {"form": form})

    # else:
    #     form = BookForm(request.POST, request.FILES)
    # return render(request, 'books/book_create.html', {"form": form})
    # return render(request, 'books/book_create.html', {"form": form})