from django.contrib import admin

from apps.orders.models import Order, OrderDish


class OrderDishInline(admin.TabularInline):
    model = OrderDish
    extra = 1  # Allows the addition of one extra empty row by default
    fields = ['dish', 'quantity']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'status', 'total_price')
    list_filter = ('status',)
    search_fields = ('table__number',)
    inlines = [OrderDishInline]  # Add inline for the OrderDish model

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        obj = form.instance
        obj.total_price = obj.calculate_total_price()
        obj.save(update_fields=['total_price'])


admin.site.register(Order, OrderAdmin)