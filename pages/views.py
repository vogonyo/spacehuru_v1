from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from listings.choices import price_choices, city_choices, bedroom_choices, category_choices
from listings.models import Listing
from realtors.models import Realtor
from django.contrib.auth.models import User
from django.views.generic import ListView
from blog.models import Blog



    
def brands(request):
    #Get All Realtors
    realtors = Realtor.objects.all()   

    context = {
        'realtors': realtors,
    
    }
    return render(request, 'pages/brands.html', context)

def tags(request):
    return render(request, 'pages/tags.html')

def blog(request):
    #Get All Realtors
    blogs = Blog.objects.all()   

    context = {
        'blogs': blogs,
    
    }
    return render(request, 'pages/blogs.html', context)

class ListingListView(ListView):
    model = Listing
    template_name = 'pages/index.html' #<app>/<model>_<vietype>.html
    context_object_name = 'listings'
    ordering = ['-list_date']
    queryset = Listing.objects.filter(is_published=True)
    paginate_by = 3

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ListingListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['price_choices'] = price_choices
        context['category_choices'] = category_choices
        context['city_choices'] = city_choices
        context['bedroom_choices'] = bedroom_choices
        return context


class UserListingListView(ListView):
    model = Listing
    template_name = 'listings/user_listings.html' #<app>/<model>_<vietype>.html
    context_object_name = 'listings'
    paginate_by = 5
   
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Listing.objects.filter(realtor=user).order_by('-list_date')

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    
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
    return render(request, 'pages/index.html', context)

def travel_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='TR').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)

def accommodation_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='AC').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)

def office_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='OF').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)

def retail_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='RE').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)


def wedding_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='WD').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)


def foodanddrink_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='FO').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)


def wellness_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='WE').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)

def storage_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='ST').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)

def popup_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='RE').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)


def shopping_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='SH').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)


def fun_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='FU').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)


def event_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='EV').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)
    
def meeting_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='ME').order_by('-list_date')

    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)

def parking_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='PA').order_by('-list_date')
    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)


def entertainment_spaces(request):
    listings = Listing.objects.filter(is_published=True, used_for='ET').order_by('-list_date')
    context = {
        'listings': listings
    }

    return render(request, 'listings/space_usage.html', context)