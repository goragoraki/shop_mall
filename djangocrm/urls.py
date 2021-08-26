from django.contrib import admin
from django.urls import path
from sales import views
from sales.views import Homepage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage)
]
