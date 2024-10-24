from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),

    path('api/v1/', include('api.urls')),

    # This is basic authetication
    #path('api/v1/auth',include('rest_framework.urls')),

    # For login, logout, password reset
    path('api/v1/auth/', include('dj_rest_auth.urls')),  
    # For registration
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),  
   
]
