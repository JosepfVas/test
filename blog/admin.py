from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_date', 'published', 'views')
    list_filter = ('created_date',)

