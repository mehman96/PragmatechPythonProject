from django.shortcuts import render


def code(request):
    return render(request, 'codes.html')

def icon(request):
    return render(request, 'icons.html')