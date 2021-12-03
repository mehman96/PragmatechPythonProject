from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request, 'single.html')

def products(request):
    return render(request, 'products1.html')

def products1(request):
    return render(request, 'products2.html')
