from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def pharmacy(request):
     return render(request, 'pharmacy.html')
 