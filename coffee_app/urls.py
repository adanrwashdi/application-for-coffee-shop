from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.coffee_detail_view.as_view(), name='coffee_detail_view'),
    path('book_table/', views.book_table_view.as_view(), name='book_table_view'),
    path('bookings/', views.booking_view.as_view(), name='booking_view'),
]