from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def manage(request):
    return render(request, 'hospital_management/base.html')

def contacts(request):
    return render(request, 'hospital_management/contacts.html')

def abouts(request):
    return render(request, 'hospital_management/abouts.html')
