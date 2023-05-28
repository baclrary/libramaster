from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import generic

from .models import CustomUser
from .forms import LoginForm, RegisterForm


def home_page(request):
    if request.user.is_anonymous:
        return render(request, 'home.html')
    return redirect("users")


def register(request):
    white_list_domains = [
        'gmail.com',
        'yahoo.com',
        'ukr.net'
    ]

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data

            email = user_data['email']
            domain = email.split('@')[-1]

            if CustomUser.get_by_email(email):
                messages.error(request, f"User with email {email} already exists.")
                return render(request, "auth/register.html", {'form': form})

            if domain not in white_list_domains:
                messages.error(request, f"Sorry, but we do not support '{domain}' domain.")
                return render(request, "auth/register.html", {'form': form})

            for field_name in ['first_name', 'middle_name', 'last_name']:
                field_length = len(user_data[field_name])
                formatted_field_name = form.fields[field_name].label

                if field_length > 20:
                    messages.error(request, f"{formatted_field_name} should not be longer than 20 characters.")
                    return render(request, "auth/register.html", {'form': form})
                elif 1 <= field_length < 3:
                    messages.error(request, f"{formatted_field_name} should be at least 3 characters.")
                    return render(request, "auth/register.html", {'form': form})

            if int(user_data['role']) == 1:
                CustomUser.objects.create_superuser(**user_data)
            else:
                CustomUser.objects.create_user(**user_data)

            messages.success(request, "Account successfully created")
            return redirect("authentication:login")
    else:
        form = RegisterForm()

    return render(request, "auth/register.html", {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users')
        else:
            messages.error(request, "Invalid email or password")
    else:
        form = LoginForm(request)

    return render(request, 'auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect("authentication:login")


class UserList(generic.ListView):
    model = CustomUser
    context_object_name = 'users'
    template_name = "auth/users_list.html"

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        query_parts = list(filter(None, query.split(' ')))

        if query:
            if len(query_parts) == 3:
                # When there are three parts in the query: full name (first name, middle name, and last name)
                users = CustomUser.objects.filter(
                    Q(first_name__icontains=query_parts[0]) &
                    Q(middle_name__icontains=query_parts[1]) &
                    Q(last_name__icontains=query_parts[2])
                ).distinct()

            elif len(query_parts) == 2:
                # When there are two parts in the query: first name and last name
                users = CustomUser.objects.filter(
                    Q(first_name__icontains=query_parts[0]) &
                    Q(last_name__icontains=query_parts[1])
                ).distinct()
            else:
                # Handle the query for other cases
                users = CustomUser.objects.filter(
                    Q(first_name__icontains=query) |
                    Q(middle_name__icontains=query) |
                    Q(last_name__icontains=query) |
                    Q(email__icontains=query)
                ).distinct()

            if not users:
                messages.error(self.request, "No user found")
            return users
        else:
            return CustomUser.get_all()


class UserDetail(generic.DetailView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'auth/user_detail.html'
