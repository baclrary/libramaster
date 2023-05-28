from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic

from .models import Author
from .forms import AuthorForm


class AuthorsList(generic.ListView):
    model = Author
    context_object_name = 'authors'
    template_name = "author/authors_list.html"

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if query:
            authors = Author.objects.filter(
                Q(name__icontains=query) |
                Q(authors__name__icontains=query) |
                Q(description__icontains=query) |
                Q(count__icontains=query)
            ).distinct()

            if not authors:
                messages.error(self.request, "No author found")
            return authors
        else:
            return Author.get_all()


class AuthorDetail(generic.DetailView):
    model = Author
    template_name = 'author/author_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_name_query = self.request.GET.get('book_name')
        author = Author.get_by_id(self.kwargs['pk'])

        if book_name_query:
            context['author_book'] = author.books.all().filter(
                Q(name__icontains=book_name_query)
            ).distinct()

            if not context['author_book']:
                messages.error(self.request, f"There's no books with name \"{book_name_query}\"")
        else:
            context['author_book'] = author.books.all()

        return context


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('author:authors')
    else:
        form = AuthorForm()

    return render(request, 'author/author_create.html', {'form': form})


def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if not author.books.exists():
        author.delete()
        messages.success(request, f"Author {author.get_full_name()} deleted successfully")
        return redirect('author:authors')
    else:
        messages.error(request,
                       "The author cannot be removed because they have one or more books associated with their account."
                       " To delete an author, all of their books must first be removed from the system.")
        return render(request, "author/author_detail.html", {"author": author})
