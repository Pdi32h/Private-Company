from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('404/', views.handler404, name='page_not_found'),
    path('product/', views.product, name='product_app'),
    path('gallery/', views.gallery, name='gallery_app'),
    path('contact/', views.contact, name='contact'),
]
