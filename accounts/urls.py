from django.urls import path
from .views import home,customer,products,create_order,update_order,delete_order,register,loginPage,logoutPage,user,user_settings

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name="home"),
    path("customer/<str:pk>/",customer,name='customer'),
    path("products/",products,name="products"),
    path('user/',user, name="user-page"),
    path('settings/',user_settings,name="settings"),

    path("create-order/<str:pk>/",create_order,name="create_order"),
    path("update-order/<str:pk>/",update_order,name="update_order"),
    path("delete/<str:pk>/",delete_order,name="delete_order"),

    path('register/',register, name="register"),
    path('login/',loginPage, name="login"),
    path('logout/',logoutPage,name='logout')
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)