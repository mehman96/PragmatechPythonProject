from django.shortcuts import render

# Create your views here.
def single (request):
    return render(request, 'single.html')

def products(request):
    return render(request, 'products.html')

def products1(request):
    return render(request, 'products1.html')

def products2(request):
    return render(request, 'products2.html')