from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request, 'product.html')

# def products(request):
#     return render(request, 'products.html')

# def product1(request):
#     return render(request, 'product1.html')

# def product2(request):
#     return render(request, 'product2.html')