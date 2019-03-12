from django.urls import path, reverse
from .views import (
    ListingListView, 
    ListingCreateView,
    ListingUpdateView,
    ListingDeleteView,
    UserListingListView,
)
from . import views

urlpatterns = [
    path('', ListingListView.as_view(), name ='listings'),
    path('user/<str:username>/', UserListingListView.as_view(), name ='user-listings'),
    path('<int:pk>/', views.listing_detail , name='listing'),
    path('<int:listing_id>/publish', views.publish, name='listing-publish'),
    path('<int:listing_id>/favourite', views.favourite, name='favourite'),
    path('<int:listing_id>/publish/pay', views.makepayment, name='make-payment'),
    path('<int:listing_id>/publish/checkout', views.checkout, name='checkout'),
    path('add/', ListingCreateView.as_view(), name='listing-create'),
    path('<int:pk>/update', ListingUpdateView.as_view(), name='listing-update'),
    path('<int:pk>/delete', ListingDeleteView.as_view(), name='listing-delete'),
    path('search', views.search, name ='search'),

]