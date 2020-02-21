from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('home')
    return render(request , 'userApps/dashboard.html')
def customers(request):
    #return HttpResponse('customers')
    return render(request , 'userApps/customers.html')

def products(request):
    #return HttpResponse('products')
    return render(request , 'userApps/products.html')
