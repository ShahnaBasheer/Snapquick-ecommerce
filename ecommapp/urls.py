from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="homepage"),
    path('accounts/login/',views.signin,name="login"),
    path('registration/',views.registration,name="registration"),
    path('logout',views.signout,name="logout"),
    path('women/',views.womentab,name="womenpage"),
    path('men/',views.mentab,name="menpage"),
    path('kids/',views.kidstab,name="kidspage"),
    path('women/filter_data',views.filter_women,name="women_filter"),
    path('men/filter_data',views.filter_men,name="men_filter"),
    path('kids/filter_data',views.filter_kids,name="kids_filter"),
    path('all-brands/',views.all_brands,name="all_brands"),
    path('all-brands/filter_data',views.filter_brands,name="filter_brands"),
    path('pro/<slug:slug>',views.product_info,name="product_info"),
    path('cart/',views.cart,name="cart"),
    path('add_to_cart/<product_id>',views.add_to_cart,name="addtocart"),
    path('update_quantity/<cart_id>',views.update_quantity,name="updateqty"),
    path('delete_quantity/<cart_id>',views.delete_quantity,name="deleteqty"),
    path('remove_cart_item/<cart_id>',views.remove_cart_item,name="remove_cartitem"),
    path('save_it_for_later/<save_id>',views.save_for_later,name="save_for_later"),
    path('remove_save_it_for_later/<save_id>',views.remove_save_later,name="remove_save_later"),
    path('move_to_cart/<move_id>',views.move_to_cart,name="move_to_cart"),
    path('search-all-category/',views.searchall,name="search_all"),
    path('search-all-category/filter_data',views.filter_search,name="search_filter"),
    path('sell',views.selleradd,name="selleradd"),
    path('user-profile/',views.profile,name="user_profile"),  
]