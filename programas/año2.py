# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:42:58 2022

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

def daysInMonth(anio,month):
	if anio < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(anio):
		res = 29
	return res

testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
	yr = testyears[i]
	mo = testmonths[i]
	print(yr,mo,"-> ",end="")
	result = daysInMonth(yr, mo)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")