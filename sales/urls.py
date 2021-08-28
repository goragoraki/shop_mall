from django.urls import path
from .views import Sales_List, Sales_Detail, Make_Sale, Sale_Update,Sale_delete

app_name = "homepage"

urlpatterns = [
    path('', Sales_List, name = 'list'),
    path('<int:pk>/', Sales_Detail, name = 'detail'), #pk (고유 id)
    path('<int:pk>/update/', Sale_Update, name = 'update'),
    path('<int:pk>/delete/', Sale_delete, name = 'delete'),
    path('make/',Make_Sale, name = 'make'),
]
