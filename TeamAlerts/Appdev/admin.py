from django.contrib import admin
from .models import Announcement

# Register your models here.

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content', 'created_at')
    readonly_fields = ('created_at',)  # If 'created_at' should be read-only
    
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('Date Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Collapsible section
        }),
    )