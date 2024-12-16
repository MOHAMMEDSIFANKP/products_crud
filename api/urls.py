from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home, name="home" ),
    path('add/', views.add_products, name="add_products" ),
    path('edit/', views.edit_product, name="edit_product" ),
]