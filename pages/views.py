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
