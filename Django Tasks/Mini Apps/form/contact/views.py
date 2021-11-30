from django import forms
from django.shortcuts import redirect, render
from . forms import ContactForm
from . models import Tags

def tags(request):
    tags=Tags.objects.all()
    context={
        'tags': tags
    }
    return render(request, 'tags.html',context)

def tags(request):
    tags=Tags.objects.all()
    context={
        'tags': tags
    }
    return render(request, 'tags.html',context)




def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'contact.html', {'form': form})