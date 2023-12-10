from django.shortcuts import render, HttpResponse
from .models import Employee
# Create your views here.

# def homepage(request):
#     print(request.method, request.user)
#     return HttpResponse("hello")


def homepage(request):
    emps = Employee.objects.all()
    # print(request.method, request.user)                                #for html page
    return render(request, "home.html", context = {"name" : ["misd", "a"], "all_emps": emps}) 

def page(request):
    return render(request, "practice.html")
# cleint (browser)> server 