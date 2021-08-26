from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Sale

# Create your views here.
def Sales_List(request):
    sales_person = Sale.objects.all()
    context = {
        "person_key" : sales_person
    }
    return render(request, "sales_list.html", context)

def Sales_Detail(request, pk):   
    sales_person = Sale.objects.get(id = pk)
    context = {
        "person_key" : sales_person
    }

    return render(request, "sales_detail.html", context)


