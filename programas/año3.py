# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:49:39 2022

@author: luise
"""

def isYearLeap(anio):
	if anio % 4 != 0:
		return False
	elif anio % 100 != 0:
		return True
	elif anio % 400 != 0:
		return False
	else:
		return True

def diasenelmes(anio, mes):
	if anio < 1582 or mes < 1 or mes > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[mes - 1]
	if mes == 2 and isYearLeap(anio):
		res = 29
	return res

def diasanio(anio, mes, dia):
	dias = 0
	for m in range(1, mes):
		md = diasenelmes(anio, m)
		if md == None:
			return None
		dias += md
	md = diasenelmes(anio, mes)
	if dia >= 1 and dia <= md:
		return dias + dia
	else:
		return None

print(diasanio(2000, 12, 31))