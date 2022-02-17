from django.contrib import admin
from .models import Coffee, CoffeeType ,WeekDays,TableType, Table
from django.utils.html import format_html

# Register your models here.


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'get_price',
        'age_limit',
        'get_days_available',
        'get_time_available',
        'type',
        'get_status',
        'created_at',
    ]
    save_as = True

    def get_price(self, ins):
        return f"{ins.price}$"
    get_price.short_description = "Price"

    def get_status(self, ins):
        return ins.get_status_display()
    get_status.short_description = "Status"

    def get_time_available(self, ins):
        if ins.available_from and ins.available_to:
            return f"From {ins.available_from} To {ins.available_to}"
        return "Always Available"
    get_time_available.short_description = "Time Available"

    def get_days_available(self, ins):
        days_available = ""
        for day in ins.days_available.all():
            days_available += f"{day.name} - "
        return days_available
    get_days_available.short_description = "Days Available"




@admin.register(CoffeeType)
class CoffeeTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]


@admin.register(WeekDays)
class WeekDaysAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]


@admin.register(TableType)
class TableTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'get_days_available',
    ]

    def get_days_available(self, ins):
        days_available = ""
        for day in ins.days_available.all():
            days_available += f"{day.name} - "
        return days_available
    get_days_available.short_description = "Days Available"


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'get_location',
        'capacity',
    ]

    def get_location(self, ins):
        return ins.get_location_display()
    get_location.short_description = "Location"


