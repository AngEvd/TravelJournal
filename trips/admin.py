from django.contrib import admin
from .models import Trip, Like

# Register your models here.
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'start_date', 'end_date', 'is_public', 'likes_count')
    list_filter = ('start_date', 'is_public')
    search_fields = ('title', 'description', 'destination')
    ordering = ('-start_date',)
    date_hierarchy = 'start_date'

    def likes_count(self, obj):
        return obj.likes.count()

    likes_count.short_description = 'Likes'

