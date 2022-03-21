# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:25:08 2022

@author: luise
"""

acl=int(input("ingrese el numero acl:"))
if acl>=1 and acl<=99:
    print("la acl es estandar")
elif acl>=100 and acl<=199:
    print("la acl es extendida")
else: 
    print("la acl no es normal")