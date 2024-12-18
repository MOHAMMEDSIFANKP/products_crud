from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home, name="home" ),
    path('signin/', views.signin, name="signin" ),
    path('signout/', views.signout, name="signout" ),
    path('add/', views.add_products, name="add_products" ),
    path('edit/<int:id>', views.edit_product, name="edit_product" ),
    path('delete/<int:id>', views.delete_products, name="delete_products" ),
]