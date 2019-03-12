from django.contrib import admin
from .models import Listing, Review

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'category', 'used_for','price', 'billing', 'list_date','created_at', 'realtor', 'get_time_diff')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'category')
    list_editable = ('is_published',)
    search_fields = ('category', 'title', 'city', 'price', 'billing', 'address')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
