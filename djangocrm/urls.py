from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from sales import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name = 'home'),
    path('Homepage/', include('sales.urls', namespace = 'homepage'))
]
