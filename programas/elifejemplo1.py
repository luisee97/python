# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:33:43 2022

@author: luise
"""

nom=input("ingrese tu nombre:")
ape=input("ingrese tu apellido:")
loca=input("ingrese tu domicilio:")
edad=input("ingrese su edad:")
space=" "
print("Su nombre es:"+nom+" "+ape+ " domicilio:" +loca+ " edad:"+edad+".")
edad=int (edad)
if edad>=1 and edad<=12:
    print("y es un niño")
elif edad>=13 and edad<=18:
    print("y es un adolecente")
elif edad>=19 and edad<=64:
    print(" adulto")
else:  
    print("fin")