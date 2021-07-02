from django.db import models

# Os banocs vão ter a mesma estrutura, mas com ´names´ diferentes.
# Na teoria, isso deve servir pra poder salvar localmente e exportar de forma remota.

class companiesKFS (models.Model):
# aqui vão os campos das ´companies´ banco da kfs
  name                     = models.CharField(max_length=255)
  has_active               = models.SmallIntegerField()
  has_active_contacts      = models.SmallIntegerField()
  has_satisfacao           = models.SmallIntegerField()
  number_users             = models.SmallIntegerField()
  old_number               = models.SmallIntegerField()
  relatorio_totalizadores  = models.SmallIntegerField()
  version                  = models.SmallIntegerField(default=3)
  active                   = models.SmallIntegerField(default=1)
  integrated_confirmations = models.SmallIntegerField()
  created                  = models.DateTimeField(auto_now_add=True)
  modified                 = models.DateTimeField(auto_now=True)

# class numbersKFS (models.Model):
# #  aqui vão os campos do banco da kfs

# class callsKFS (models.Model):
# #  aqui vão os campos do banco da kfs

# class modules_has_companiesKFS (models.Model):
# #  aqui vão os campos do banco da kfs

# class quick_answersKFS (models.Model):
# #  aqui vão os campos do banco da kfs

# class scriptsKFS (models.Model):
# #  aqui vão os campos do banco da kfs

# class usersKFS (models.Model):
# #  aqui vão os campos do banco da kfs

# class tagsKFS (models.Model):
# #  aqui vão os campos do banco da kfs