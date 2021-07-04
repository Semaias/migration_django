from django.shortcuts import render
from .models import Companies
from django.http import HttpResponse

# Create your views here.
    
# write
def someview ():
    com = Companies.objects.filter(active=1)
    
    

    try:
        file = open('arquivo.txt', 'a')
    except:
        file = open('arquivo.txt', 'w')

    # id, name, has_active, has_active_contacts, has_satisfacao, number_users, 
    # old_number, relatorio_totalizadores, version, active, 
    # integrated_confirmations, created, modified

    for x in com:

        arquivo.write(str(x.id)+"$"+str(x.name)+"$"+str(x.has_active)+"$"+str(x.has_active_contacts)+"$"+str(x.has_satisfacao)+"$"+str(x.number_users)+"$"+str(x.old_number)+"$"+str(x.relatorio_totalizadores)+"$"+str(x.version)+"$"+str(x.active)+"$"+str(x.integrated_confirmations)+"$"+str(x.created)+"$"+str(x.modified))
        arquivo.write("\n")

    arquivo.close()

    return HttpResponse("GET")

# ler
def anyview ():
    file = open('arquivo.txt', 'r')

 
    # e_id = None, name = None, relatorio_totalizadores = None, version = None, active = None, integrated_confirmations = None
    # created = None, modified = None
    
    for line in file:
        for char in line:
            if (char != "$") :
                e_id += char
            else: 
                if (char != "$"):
                    name += char 
                else:
                    if (char != "$"):
                        has_active += bool(char)
                    else:
                        if (char != "$"):
                            has_active_contacts += bool(char)
                        else:
                            if (char != "$"):
                                has_satisfacao += bool(char)
                            else:
                                if (char != "$"):
                                    number_users += int(char)
                                else:
                                    if (char != "$"):
                                        old_number += int(char)
                                    else: 
                                        if (char != "$"):
                                            relatorio_totalizadores += str(char)
                                        else:
                                            if(char != "$"):
                                                version += str(char)
                                            else:
                                                if(char != "$"):
                                                    active += str(char)
                                                else:
                                                    if(char != "$"):
                                                        integrated_confirmations += str(char)
                                                    else:
                                                        if(char != "$"):
                                                            created += str(char)
                                                        else:
                                                            if(char != "$"):
                                                                modified += str(char)


        # id, name, has_active, has_active_contacts, has_satisfacao, number_users, 
        # old_number, relatorio_totalizadores, version, active, 
        # integrated_confirmations, created, modified
        com = Companies.objects.create(id=e_id, name=name, has_active=has_active, has_active_contacts=has_active_contacts, has_satisfacao=has_satisfacao, number_users=number_users, old_number=old_number, relatorio_totalizadores=relatorio_totalizadores, version=version, active=active, integrated_confirmations=integrated_confirmations, created=created, modified=modified)

    return HttpResponse("POST")


# AVISO, LEIA OU MORRA

# SÓ USE A VIEW SOMEVIEW (GET) SE ESTIVER CONECTADO AO BANCO QUE VOCÊ QUER COPIAR
# SÓ USE A VIEW ANYVIEW (POST) SE ESTIVER CONECTADO AO BANCO CÓPIA
# QUALQUER DÚVIDA, DEPOIS TU FALA, PROVAVELMENTE VAI DAR ALGUM ERRO NESSES IF'S, VEMOS ISSO DEPOIS