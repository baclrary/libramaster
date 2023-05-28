from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import generic
from .models import Order
from authentication.models import CustomUser
from book.models import Book
from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderForm


class OrdersList(LoginRequiredMixin, generic.ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'order/orders_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        query_parts = list(filter(None, query.split(' ')))
        if query:
            if len(query_parts) == 3:
                # handle full name input
                orders = Order.objects.filter(
                    Q(book__name__icontains=query) |
                    (Q(user__first_name__icontains=query_parts[0]) &
                     Q(user__middle_name__icontains=query_parts[1]) &
                     Q(user__last_name__icontains=query_parts[2])) |
                    Q(created_at__icontains=query) |
                    Q(end_at__icontains=query) |
                    Q(plated_end_at__icontains=query)
                ).distinct()

            elif len(query_parts) == 2:
                # handle first and last name input
                orders = Order.objects.filter(
                    Q(book__name__icontains=query) |
                    (Q(user__first_name__icontains=query_parts[0]) &
                     Q(user__last_name__icontains=query_parts[1])) |
                    Q(created_at__icontains=query) |
                    Q(end_at__icontains=query) |
                    Q(plated_end_at__icontains=query)
                ).distinct()
            else:
                # Handle the rest
                orders = Order.objects.filter(
                    Q(book__name__icontains=query) |
                    Q(user__first_name__icontains=query) |
                    Q(user__middle_name__icontains=query) |
                    Q(user__last_name__icontains=query) |
                    Q(created_at__icontains=query) |
                    Q(end_at__icontains=query) |
                    Q(plated_end_at__icontains=query)
                ).distinct()


            if not orders:
                messages.error(self.request, "No orders found")
            return orders
        else:
            return Order.get_all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_orders'] = Order.objects.filter(user=self.request.user)
        return context


class OrderDetail(LoginRequiredMixin, generic.DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'order/order_detail.html'

    def get_queryset(self):
        # Filter orders based on the currently logged-in user
        if self.request.user.role == 0:
            return Order.objects.filter(user=self.request.user)
        else:
            return Order.objects.all()



def close_order(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.close()

    return render(request, 'order/order_detail.html', {'order': order})


def create_order(request, book_id=None):

    if request.user.role == 1:
        return redirect("orders:orders")

    def process_date_and_time(date_obj, time_obj):
        now = datetime.now()

        # if not manually entered data set deadline in 2 weeks
        if date_obj is None:
            date = now + timedelta(weeks=2)
        else:
            if time_obj is None:
                # midnight
                date = datetime.combine(date_obj, datetime.min.time())
                date = date.replace(hour=0, minute=0, second=0, microsecond=0)
            else:
                date = datetime.combine(date_obj, time_obj)

        return date

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            date_obj = form.cleaned_data.get('date')
            time_obj = form.cleaned_data.get('time')
            book = form.cleaned_data.get('book')

            # Check book stock
            if book.count <= 1:
                messages.error(request, 'Too few books in stock')
                return render(request, 'order/order_create.html', {"form": form, "book_id": book_id})

            # Check if user already ordered the book and hasn't returned it yet
            if book in request.user.get_books():
                messages.error(request,
                               f'User {request.user.get_full_name()} already ordered book "{book.name}" and haven\'t returned it yet')
                return render(request, 'order/order_create.html', {"form": form, "book_id": book_id})

            order = form.save(commit=False)
            order.user = request.user
            order.plated_end_at = process_date_and_time(date_obj, time_obj)
            # order.save()
            Order.create(user=order.user, book=order.book, plated_end_at=order.plated_end_at)
            messages.success(request, "Order registered successfully.")
            return redirect('orders:orders')
        else:
            messages.error(request, "Failed to register the order. Please check the form for errors.")
    else:
        form = OrderForm(initial={'book': book_id})

    return render(request, 'order/order_create.html', {"form": form, "books": Book.get_all(), "book_id": book_id})
