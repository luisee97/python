# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:18:05 2022

@author: luise
"""

def isYearLeap (año) :
  if año % 4 != 0:
    return False
  elif año % 100 != 0:
    return True 
  elif año % 400 != 0:
    return False 
  else:
    return True 

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
  yr = testData[i]
  print(yr,"->",end="")
  result = isYearLeap(yr)
  if result == testResults[i]:
    print("OK")
  else:
    print("Failed")