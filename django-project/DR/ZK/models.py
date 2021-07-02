from django.db import models

# Create your models here.

# app/models.py:
class MigrationKFSM3 (models.Model):
  # .....
    
  # app/dbrouters.py: # [new file]
from .models import MigrationKFSM3
  
class DBRouter:
  def db_for_read (self, model, **hints):
    if (model == kfs):
      # your model name as in settings.py/DATABASES
      return 'kfs'
    return None
       
  def db_for_write (self, model, **hints):
    if (model == m3):
      # your model name as in settings.py/DATABASES
      return 'm3'
    return None