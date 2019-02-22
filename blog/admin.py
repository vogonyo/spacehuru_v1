from django.contrib import admin
from .models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 25

admin.site.register(Blog, BlogAdmin)