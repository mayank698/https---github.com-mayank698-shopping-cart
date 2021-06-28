from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('', views.index,name="Home"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('track_order', views.tracker,name="tracker"),
    path('search', views.search,name="search"),
    path('product_view/<int:myid>', views.product_view,name="product_view"),
    path('checkout', views.checkout,name="checkout"),
]
