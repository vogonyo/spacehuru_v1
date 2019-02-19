from django.urls import path, reverse
from .views import (
    ListingListView, 
    ListingDetailView, 
    ListingCreateView,
    ListingUpdateView,
    ListingDeleteView,
    UserListingListView
)
from . import views

urlpatterns = [
    path('', ListingListView.as_view(), name ='listings'),
    path('user/<str:username>/', UserListingListView.as_view(), name ='user-listings'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing'),
    path('<int:listing_id>/publish', views.publish, name='listing-publish'),
    path('add/', ListingCreateView.as_view(), name='listing-create'),
    path('<int:pk>/update', ListingUpdateView.as_view(), name='listing-update'),
    path('<int:pk>/delete', ListingDeleteView.as_view(), name='listing-delete'),
    path('inquiries', views.inquiries, name ='inquiries'),
    path('search', views.search, name ='search'),

]