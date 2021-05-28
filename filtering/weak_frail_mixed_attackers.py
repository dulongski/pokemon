# -*- coding: utf-8 -*-
"""
Created on Sun May 23 01:09:13 2021

@author: ssds6
"""
import pandas as pd

data = pd.read_csv('C:/Users/ssds6/Downloads/Pokemon.csv') #importar desde la dirección donde tengas la database

data_list = data.values.tolist()

DIF_ATKS = .7916
MIN_ATKS = 90
CUT_SLOW = 70 #luxray
CUT_FRAIL = 253 #decidueye

##funciones para max y min
def maxim(a, b):
    if a > b:
        return a
    return b
def minim(a, b):
    if a < b:
        return a
    return b

##si un poke es mixed attacker
def mixed_attacker(l):
    maxx = maxim(l[6],l[8])
    minn = minim(l[6],l[8])
    if minn>=DIF_ATKS*maxx and minn>=MIN_ATKS:
        return True
    return False

##si un poke es mixed attacker con atk = spatk
def mixed_strict(l):
    if l[6]==l[8]:
        return True
    return False

def slow(l):
    if l[10]<=CUT_SLOW:
        return True
    return False

def frail(l):
    if l[5]+l[7]+l[9]<=CUT_FRAIL:
        return True
    return False

l1 = []
            
for l in data_list:
    if mixed_attacker(l) and slow(l) and frail(l):
        l1.append(l)
        print(l)
