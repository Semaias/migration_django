from django.shortcuts import render
from .models import MigrationKFSM3
# Create your views here.

def someotherview (request):
  # You can even use the following:
  kfs = KFS(
    email="<email>",
    phone="<phone>",
    # .....
  )