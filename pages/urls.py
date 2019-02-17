from django.urls import path
from .views import ListingListView
from . import views

urlpatterns = [
    path('', ListingListView.as_view(), name ='index'),
    path('about', views.about, name='about'),
]