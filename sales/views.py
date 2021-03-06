from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Sale, Person
from .forms import SaleForm, SaleModelForm
from django.views import generic
# Create your views here.

class Home_V(generic.TemplateView):
    template_name ="home.html"

def Home(request):
    return render(request, "home.html")

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

##모델 폼
def Make_Sale(request):
    v_form = SaleModelForm
    if request.method == "POST":
        v_form = SaleModelForm(request.POST)
        if v_form.is_valid():
            v_form.save()
            return redirect("homepage:list")
            
    context ={
        "forms_key" : v_form
    }

    return render(request, "make_sale.html", context)

##모델폼
def Sale_Update(request, pk):
    person = Sale.objects.get(id=pk)

    v_form = SaleModelForm(instance=person)
    if request.method == "POST":
        v_form = SaleModelForm(request.POST, instance=person)
        if v_form.is_valid():
            v_form.save()
            return redirect("homepage:list")

    context ={
        'person_key' : person,
        "forms_key" : v_form,
    }
    return render(request, "sales_update.html", context)

def Sale_delete(request, pk):
    person = Sale.objects.get(id=pk)
    person.delete()
    return redirect('homepage:list')



##일반폼
""" def Sale_Update(request, pk):
    person = Sale.objects.get(id=pk)
    v_form = SaleForm()
    if request.method == "POST":
        v_form = SaleForm(request.POST)
        if v_form.is_valid():
            first_name_ = v_form.cleaned_data['first_name']
            last_name_ = v_form.cleaned_data['last_name']
            age_ = v_form.cleaned_data['age']

            person.first_name = first_name_
            person.last_name = last_name_
            person.age = age_
            person.save()
            return redirect("/Homepage")

    context ={
        'person_key' : person,
        "forms_key" : v_form,
    }
    return render(request, "sales_update.html", context) """

## 그냥 폼
""" def Make_Sale(request):
    v_form = SaleForm()
    if request.method == "POST":
        print("post message")
        v_form = SaleForm(request.POST)
        if v_form.is_valid():
            print("ok")
            print(v_form.cleaned_data)
            first_name_ = v_form.cleaned_data['first_name']
            last_name_ = v_form.cleaned_data['last_name']
            age_ = v_form.cleaned_data['age']
            person_  = Person.objects.first()

            Sale.objects.create(
                first_name = first_name_,
                last_name = last_name_,
                age = age_,
                person = person_,
            )
            print("input sale")

            return redirect("/Homepage")
    context ={
        "forms_key" : v_form
    }

    return render(request, "make_sale.html", context) """