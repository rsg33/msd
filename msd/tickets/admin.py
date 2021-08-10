from django.contrib import admin

from .models import Tickets, Category, State, Priority


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'author', 'title', 'content', 'category', 'state', 'priority', 'assigned', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('author', 'category', 'state')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class PriorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Tickets, TicketAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Priority, PriorityAdmin)