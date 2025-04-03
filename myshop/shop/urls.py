from django.urls import path, include
from . import views

app_name = 'shop'  # Add this line to specify the app name


urlpatterns = [
    path('', views.product_list, name='product_list'),  # For homepage
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),  # For category-based list
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),  # For product details
]
