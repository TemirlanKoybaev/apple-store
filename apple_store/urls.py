from django.contrib import admin
from django.urls import path
from shop import views as shop_views
from cart import views as cart_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', accounts_views.register, name='register'),
    path('login/', accounts_views.user_login, name='login'),
    path('logout/', accounts_views.user_logout, name='logout'),
    path('profile/', accounts_views.profile, name='profile'),

    path('cart/', cart_views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', cart_views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_views.cart_remove, name='cart_remove'),

    # Магазин
    path('', shop_views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', shop_views.product_list, name='product_list_by_category'),

    # Контакты (черновик)
    path('contacts/', shop_views.contact_page, name='contact_page'),

    path('<slug:slug>/', shop_views.product_detail, name='product_detail'),
]