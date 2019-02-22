from django.urls import path
from .views import ListingListView
from . import views

urlpatterns = [
    path('', ListingListView.as_view(), name ='index'),
    path('brands', views.brands, name='brands'),
    path('blog', views.blog, name='blog'),

]