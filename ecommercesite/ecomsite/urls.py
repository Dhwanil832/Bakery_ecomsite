from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('clearcart/', views.clerarcart, name='clearcart'),
    path('clearlist/', views.clerarlist, name='clearlist'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('product/', views.product, name='product'),
    path('product/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('product/add_to_wish', views.add_to_wish, name='add_to_wish'),
    path('product/category', views.productcategory, name='productcategory'),
    path('flashsale/', views.flashsale, name='flashsale'),
    path('seasonalpromotion/', views.seasonalpromotion, name='seasonalpromotion'),
    path('productdetail/<int:id>', views.productdetail, name='productdetail'),
    path('delete_crt_item/<int:id>', views.delete_crt_item, name='delete_crt_item'),
    path('delete_list_item/<int:id>', views.delete_list_item, name='delete_list_item'),
    path('cart_info', views.cart_info, name='cart_info'),
    path('productdetail/get_recent_products/',views.compare, name="get_recent_products"),
    path('search/',views.search, name="search"),
    
]