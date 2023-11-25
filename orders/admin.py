from django.contrib import admin
from .models import SalesOrder, Place, Restaurant, Waiter


@admin.register(SalesOrder)
class AdminSalesOrder(admin.ModelAdmin):
    list_display = (
        'amount',
        'description',
    )


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
    )


@admin.register(Restaurant)
class AdminRestaurant(admin.ModelAdmin):
    list_display = (
        'place',
        'serves_hot_dogs',
        'serves_pizza',
    )


@admin.register(Waiter)
class AdminRestaurant(admin.ModelAdmin):
    list_display = (
        'restaurant',
        'name',
    )
