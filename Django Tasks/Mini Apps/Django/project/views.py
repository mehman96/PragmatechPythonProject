from django.shortcuts import render
# hhtp respons import etdik
from django.http import HttpResponse
# Create your views here.


# project adinda funksiya yazdiq
def project(request):
    return HttpResponse("My first django project")

def about(request):
    return HttpResponse("about page")