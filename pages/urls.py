from django.urls import path
from .views import ListingListView
from . import views

urlpatterns = [
    path('', ListingListView.as_view(), name ='index'),
    path('brands', views.brands, name='brands'),
    path('blog', views.blog, name='blog'),
    path('travel', views.travel_spaces, name='travel-spaces'),
    path('accommodation', views.accommodation_spaces, name='accommodation-spaces'),
    path('officeandcowork', views.office_spaces, name='office-spaces'),
    path('popupshops', views.retail_spaces, name='retail-spaces'),
    path('weddings', views.wedding_spaces, name='wedding-spaces'),
    path('foodanddrink', views.foodanddrink_spaces, name='foodanddrink-spaces'),
    path('wellness', views.wellness_spaces, name='wellness-spaces'),
    path('experiences', views.fun_spaces, name='fun-spaces'),
    path('shopping', views.shopping_spaces, name='shopping-spaces'),
    path('storage', views.storage_spaces, name='storage-spaces'),
    path('popup', views.popup_spaces, name='popup-spaces'),
    path('events', views.event_spaces, name='event-spaces'),
    path('meetings', views.meeting_spaces, name='meeting-spaces'),
    path('parking', views.meeting_spaces, name='parking-spaces'),
    path('entertainment', views.meeting_spaces, name='entertainment-spaces'),


]
