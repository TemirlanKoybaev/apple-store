from django.contrib import admin
from django.urls import path, include  
from shop import views as shop_views
from cart import views as cart_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Авторизация
    path('register/', accounts_views.register, name='register'),
    path('login/', accounts_views.user_login, name='login'),
    path('logout/', accounts_views.user_logout, name='logout'),
    path('profile/', accounts_views.profile, name='profile'),
    
    # Корзина
    path('cart/', cart_views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', cart_views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_views.cart_remove, name='cart_remove'),
    
    # Заказы
    path('orders/', include('orders.urls')),  
    
    # Магазин
    path('', shop_views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', shop_views.product_list, name='product_list_by_category'),
    path('<slug:slug>/', shop_views.product_detail, name='product_detail'),
]