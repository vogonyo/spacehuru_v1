from django.urls import path
from .views import ListingListView
from . import views

urlpatterns = [
    path('', ListingListView.as_view(), name ='index'),
    path('brands', views.brands, name='brands'),
    path('blog', views.blog, name='blog'),
    path('tag/travel', views.travel_spaces, name='travel-spaces'),
    path('tag/accommodation', views.accommodation_spaces, name='accommodation-spaces'),
    path('tag/officeandcowork', views.office_spaces, name='office-spaces'),
    path('tag/popupshops', views.retail_spaces, name='retail-spaces'),
    path('tag/weddings', views.wedding_spaces, name='wedding-spaces'),
    path('tag/foodanddrink', views.foodanddrink_spaces, name='foodanddrink-spaces'),
    path('tag/wellness', views.wellness_spaces, name='wellness-spaces'),
    path('tag/experiences', views.fun_spaces, name='fun-spaces'),
    path('tag/shopping', views.shopping_spaces, name='shopping-spaces'),
    path('tag/storage', views.storage_spaces, name='storage-spaces'),
    path('tag/popup', views.popup_spaces, name='popup-spaces'),
    path('tag/entertainment', views.entertainment_spaces, name='entertainment-spaces'),
]
