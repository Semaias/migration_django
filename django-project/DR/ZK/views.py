from django.shortcuts import render
from .models import companiesKFS
# Create your views here.
    
def someview ():
  obj = companiesKFS.objects.get(id>1)