from django.http.response import HttpResponse
from django.shortcuts import render
from .models import 아이디

# Create your views here.
def Homepage(request):
    custom = 아이디.objects.all()
    context = {
        "menu" : "bread",
        "price" : "600won",
        "custom" : custom ,
    }
    return render(request, "index2.html", context)

