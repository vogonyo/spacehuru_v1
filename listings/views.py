from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.models import User
from .choices import price_choices, city_choices, bedroom_choices, category_choices
from .models import Listing
from django.urls import reverse
from users.models import Profile

class ListingListView(ListView):
    model = Listing
    template_name = 'listings/listings.html' #<app>/<model>_<vietype>.html
    context_object_name = 'listings'
    ordering = ['-list_date']
    queryset = Listing.objects.filter(is_published=True)
    paginate_by = 3
    

class UserListingListView(ListView):
    model = Listing
    template_name = 'listings/user_listings.html' #<app>/<model>_<vietype>.html
    context_object_name = 'listings'
    paginate_by = 5
   
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Listing.objects.filter(realtor=user).order_by('-list_date')

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listings/listing.html'

class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    fields = ['category', 'title', 'address', 'area', 'city', 'description', 'price', 'billing', 'bedrooms','sqft', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6']

    def form_valid(self, form):
        form.instance.realtor = self.request.user
        return super().form_valid(form)
    

    

class ListingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Listing
    fields = ['category', 'title', 'address', 'area', 'city', 'description', 'price', 'billing', 'bedrooms', 'sqft', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6']

    def form_valid(self, form):
        form.instance.realtor = self.request.user
        return super().form_valid(form)

    
    def test_func(self):
        listing = self.get_object()
        if self.request.user == listing.realtor:
            return True
        return False

class ListingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Listing
    success_url = '/dashboard'
    
    def test_func(self):
        listing = self.get_object()
        if self.request.user == listing.realtor:
            return True
        return False

class DashboardListingListView(LoginRequiredMixin, ListView):
    model = Listing
    template_name = 'users/user_dashboard.html' #<app>/<model>_<vietype>.html
    context_object_name = 'listings'
    ordering = '-list_date'
    paginate_by = 6
   
    def get_queryset(self):
        queryset = super(DashboardListingListView, self).get_queryset()
        queryset = queryset.filter(realtor=self.request.user)
        return queryset

class FavouriteListingListView(LoginRequiredMixin, ListView):
    model = Listing
    template_name = 'users/user_favourites.html'
    context_object_name = 'listing'
    ordering = '-list_date'
    paginate_by = 6


def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)

    
    #city
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__iexact=category)

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)



    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    
    #area
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            queryset_list = queryset_list.filter(area__iexact=area)

    
    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
     
    
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    
    
    context = {
        'listings': queryset_list,
        'city_choices': city_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'category_choices': category_choices
    }
    return render(request, 'listings/search.html', context)


def publish(request, listing_id):
    if request.method == 'POST':
        listing = get_object_or_404(Listing, pk=listing_id)
        listing.is_published = True
        listing.save()
        messages.success(request, 'Your listing is now active!')
        return redirect('/listings/')

