from django.shortcuts import render
from .models import companiesKFS
# Create your views here.
    
def someview ():
  cKFS = companiesKFS.objects.all()