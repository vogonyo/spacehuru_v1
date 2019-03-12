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
from django.contrib.auth.decorators import login_required
from .choices import price_choices, city_choices, bedroom_choices, category_choices
from .models import Listing, Review
from .payments import simulatePayment, query
from django.urls import reverse
from users.models import Profile
from contacts.models import Contact
import datetime
import urllib.request

class ListingListView(ListView):
    model = Listing
    template_name = 'listings/listings.html' #<app>/<model>_<vietype>.html
    context_object_name = 'listings'
    ordering = ['-list_date']
    queryset = Listing.objects.filter(is_published=True)
    paginate_by = 6


class UserListingListView(ListView):
    model = Listing
    template_name = 'listings/user_listings.html' #<app>/<model>_<vietype>.html
    context_object_name = 'listings'
    paginate_by = 5
   
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Listing.objects.filter(realtor=user).order_by('-list_date')


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, id=pk)
    is_favourite = False
    if listing.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    context = {
        'listing': listing,
        'is_favourite': is_favourite
    }

    return render(request, 'listings/listing.html', context)

class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    fields = ['category', 'used_for', 'title', 'address', 'area', 'city', 'description', 'price', 'billing', 'bedrooms','sqft', 'is_available', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6']
    success_url = '/dashboard'
    
    def form_valid(self, form):
        form.instance.realtor = self.request.user
        return super().form_valid(form)
    

    

class ListingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Listing
    fields = ['category', 'used_for', 'title', 'address', 'area', 'city', 'description', 'price', 'billing', 'bedrooms', 'sqft', 'is_available', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6']

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
    paginate_by = 3
   
    def get_queryset(self):
        queryset = super(DashboardListingListView, self).get_queryset()
        queryset = queryset.filter(realtor=self.request.user)
        return queryset

def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    #city
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            paginator = Paginator(queryset_list.filter(category__iexact=category), 6)
            page = request.GET.get('page')
            paged_listings = paginator.get_page(page)

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            paginator = Paginator(queryset_list.filter(description__icontains=keywords), 6)
            page = request.GET.get('page')
            paged_listings = paginator.get_page(page)


    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            paginator = Paginator(queryset_list.filter(city__iexact=city), 6)
            page = request.GET.get('page')
            paged_listings = paginator.get_page(page)
    
    #area
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            paginator = Paginator(queryset_list.filter(area__iexact=area), 6)
            page = request.GET.get('page')
            paged_listings = paginator.get_page(page)
    
    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            paginator = Paginator(queryset_list.filter(bedrooms__lte=bedrooms), 6)
            page = request.GET.get('page')
            paged_listings = paginator.get_page(page)
     
    
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            paginator = Paginator(queryset_list.filter(price__lte=price), 6)
            page = request.GET.get('page')
            paged_listings = paginator.get_page(page)
    
    
    context = {
        'listings': paged_listings,
        'city_choices': city_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'category_choices': category_choices
    }
    return render(request, 'listings/search.html', context)


def publish(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
      'listing': listing
    }
    return render(request, 'listings/payments.html', context)

def makepayment(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    
    context = {
      'listing': listing
    }
    return render(request, 'listings/checkout.html', context)

def checkout(request, listing_id):
    if request.method == 'POST':
        phone = request.POST['phone']
        simulatePayment(phone)
        response = urllib.request.urlopen('https://darajambili.herokuapp.com/callback')
        html = response.read()
        listing = get_object_or_404(Listing, pk=listing_id)
        listing.is_published = True
        listing.created_at = datetime.datetime.now()
        listing.save()
        messages.success(request, 'Payment successful, listing is now Active')
        return redirect('/spaces/')
    else:
        messages.error(request, 'Your payment was not successful')
        return redirect('/dashboard/')

@login_required
def bookings(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'users/user_bookings.html', context)

@login_required
def wishlist(request):
    wishlist = request.user.favourite.all()
    paginator = Paginator(wishlist, 3)
    page = request.GET.get('page')
    paged_wishlist = paginator.get_page(page)
    
    context = {
        'wishlist': paged_wishlist
    }

    return render(request, 'listings/wishlist.html', context)
        
@login_required
def favourite(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if listing.favourite.filter(id=request.user.id).exists():
        listing.favourite.remove(request.user)
    else:
        listing.favourite.add(request.user)
    return HttpResponseRedirect(listing.get_absolute_url())
    