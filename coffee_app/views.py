# Create your tests here.
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from .models import Coffee, Table
from users.decorators import allowed_users


class coffee_detail_view(View):
    def get(self, request, id):
        coffee = get_object_or_404(Coffee, id=id)
        context = {
            'coffee': coffee,
        }
        return render(request, 'coffee_app/coffee_detail.html', context)
    def post(self, request, id):
        coffee = get_object_or_404(Coffee, id=id)
        form = PayPalPaymentsForm(initial={
                "business": 'aneeqakbqr@gmail.com',
                "amount": {{20}},
                "currency_code": "EUR",
                "item_name": 'Example item',
                "invoice": 1234,
                "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
                "return_url": self.request.build_absolute_uri(reverse('paypal-return')),
                "cancel_return": self.request.build_absolute_uri(reverse('paypal-cancel')),
                "lc": 'EN',
                "no_shipping": '1',
            })
        context = {
            'coffee': coffee,
            'form': form,
        }
        return render(request, 'coffee_app/paypal_form.html', context)


class book_table_view(View):
    @allowed_users(allowed_roles=['client'])
    def get(self, request):
        table_id = request.GET.get("table_id", None)
        time = request.GET.get("time", None)
        day = request.GET.get("day", None)
        action = request.GET.get("action", None)

        if action == "book":
            table, created = Table.objects.get_or_create(booking_time=time, day=day)
            if table.booked:
                messages.error(request, "Already Booked")
            else:
                table.booked_by = request.user
                table.booked = True
                table.save()
                messages.success(request, "Successfully booked")
        elif action == "unbook":
            table = get_object_or_404(Table, id = table_id)
            if table.booked_by == request.user:
                table.booked_by = None
                table.booked = False
                table.save()
                messages.success(request, "Successfully Unbooked")

        return render(request, 'coffee_app/reservation.html')

class booking_view(View):
    @allowed_users(allowed_roles=['bariast'])
    def get(self, request):
        bookings = Table.objects.filter(booked=True)
        context = {'bookings': bookings}
        return render(request, 'store/list-all-booking.html', context)

    def post(self, request):
        table_id = request.POST.get("table_id", None)
        action = request.POST.get("action", None)

        table = get_object_or_404(Table, id = table_id)
        if action == "cancel":
            table.booked_by = None
            table.booked = False
            table.save()
            messages.success(request, "Booking Cancelled Successfully")
        return redirect("booking_view")




