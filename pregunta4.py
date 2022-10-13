# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 08:30:37 2022

@author: DELL
"""

from kanren import run, var, eq, Relation, facts
a = var()
b = var()

padre = Relation()
primo = Relation()
tio = Relation()
facts(padre, ("Heriberto P","Enrique H"),("Heriberto P","Jose H"),("Heriberto P","Maya H"),
      ("Delia P","Enrique H"),("Delia P","Jose H"),("Delia P","Maya H"))
facts(primo, ("Jose H","Eynar Pr"),("Jose H","Ericka Pr"),("Jose H","Camila Pr"),
      ("Jose H","Thiago Pr"),("Jose H","Franco Pr"))
facts(tio, ("Jose H","Hector T"),("Jose H","Rosmery T"),("Jose H","Virginia T"),
      ("Jose H","Amelia T"),("Jose H","Herminia T"),("Jose H","Lizbeth T"))

print(padre.facts)
print(run(1,a,padre(a,"Jose H")))
print(run(1,a,padre(a,"Enrique H")))
print(run(2,b,padre("Delia P",b)))
print(run(3,b,padre("Heriberto P",b)))
#print(run(3,b,padre("Maya H",b)))

print(run(3,a,primo(a,"Eynar Pr")))
print(run(3,a,primo(a,"Ericka Pr")))
print(run(3,a,primo(a,"Thiago Pr")))
print(run(3,a,primo("Jose",a)))

print(run(3,a,tio(a,"Hector T")))
print(run(3,a,tio(a,"Amelia T")))