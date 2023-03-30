from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.
"""
    ==> to store data in model 
    models.objects.create(feildname = value)

    ==. TO FETCH ALL data from model 
    model.objects.all()

    ==> fetch specific data from conditionwise from the model (result expected queryset)
    model.object.filter(fieldname = searchvalue)
"""
def home(request):
    return render(request, "myapp/index.html")

def about(request):
    return HttpResponse("<h1>About</h1>")

def add_student(request):
    if request.POST:
        name = request.POST['name']
        city = request.POST['city']

        sid = student.objects.create(name = name, city = city)

    return render(request, "myapp/index.html")

def all_student(request):
    sall = student.objects.all()
    print("====> sall",sall)
    context = {
        'sall' : sall
    }
    return render(request, "myapp/all_student.html",context)

def search_student(request):
    if request.POST:
        cityname = request.POST['city']
        sall = student.objects.filter(city = cityname)
        print("===> sall",sall)
        context = {
            'sall' : sall
        }
        return render(request, "myapp/all_student.html",context)
    else:
        sall = student.objects.all()
        print("===> sall",sall)
        context = {
            'sall' : sall
        }
        return render(request, "myapp/all_student.html",context)
    
def del_student(request, pk):
    print(pk)
    return render(request, "myapp/all_student.html")


