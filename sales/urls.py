from django.urls import path
from .views import Sales_List, Sales_Detail

app_name = "homepage"

urlpatterns = [
    path('', Sales_List),
    path('<pk>/', Sales_Detail), #pk (고유 id)
]
