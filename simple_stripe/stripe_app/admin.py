from django.contrib import admin

from stripe_app.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    ordering = ('name', )
