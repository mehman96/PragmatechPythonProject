from django.shortcuts import render
from .models import Blog
from django.db.models import Sum,Min,Max,Avg

# Create your views here.

def index(request):
    return render(request, 'index.html')

