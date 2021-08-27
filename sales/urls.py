from django.urls import path
from .views import Sales_List, Sales_Detail, Make_Sale

app_name = "homepage"

urlpatterns = [
    path('', Sales_List),
    path('<int:pk>/', Sales_Detail), #pk (고유 id)
    path('make/',Make_Sale),
]
