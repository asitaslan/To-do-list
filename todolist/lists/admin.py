from django.contrib import admin

# Register your models here.
from lists.models import Items, Lists


class ListsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','status', 'created_at','deadline']


admin.site.register(Lists,ListsAdmin)
admin.site.register(Items,ItemAdmin)