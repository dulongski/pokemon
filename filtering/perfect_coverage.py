# -*- coding: utf-8 -*-
"""
Created on Thu May 27 03:38:34 2021

@author: ssds6
"""

import itertools
import pandas as pd

data = pd.read_csv('C:/Users/ssds6/Downloads/Pokemon.csv') #importar del directorio donde tengas la db

data_list = data.values.tolist()

##pokemon_types y type_chart obtenidos de https://steemit.com/pokemon/@dkmathstats/generating-a-pokemon-types-table-in-python
pokemon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                 "Fighting", "Poison", "Ground", "Flying", "Psychic",
                 "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

type_chart=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
            [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
            [1, 2, 1/2, 1, 1/2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1/2, 1, 1, 1],
            [1, 1, 2, 1/2, 1/2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1/2, 1, 1, 1],
            [1, 1/2, 2, 1, 1/2, 1, 1, 1/2, 2, 1/2, 1, 1/2, 2, 1, 1/2, 1, 1/2, 1],
            [1, 1/2, 1/2, 1, 2, 1/2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1/2, 1],
            [2, 1, 1, 1, 1, 2, 1, 1/2, 1, 1/2, 1/2, 1/2, 2, 0, 1, 2, 2, 1/2],
            [1, 1, 1, 1, 2, 1, 1, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 1, 0, 2],
            [1, 2, 1, 2, 1/2, 1, 1, 2, 1, 0, 1, 1/2, 2, 1, 1, 1, 2, 1],
            [1, 1, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1/2, 1],
            [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1/2, 1, 1, 1, 1, 0, 1/2, 1],
            [1, 1/2, 1, 1, 2, 1, 1/2, 1/2, 1, 1/2, 2, 1, 1, 1/2, 1, 2, 1/2, 1/2],
            [1, 2, 1, 1, 1, 2, 1/2, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 1/2, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1/2, 0],
            [1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1/2],
            [1, 1/2, 1/2, 1/2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1/2, 2],
            [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]]

#regresa el indice del array pokemon_types dado el nombre del tipo
def type_index(type):
    return pokemon_types.index(type)

#convertimos a set para poder usar itertools.combinations
s = set(pokemon_types)

#para hacer subconjuntos de tipos
def find_subsets(s, n):
    return list(itertools.combinations(s, n))

#si un poke es debil a cierto tipo de ataque
def weak_to_type(pok, att_type):
    if not isinstance(pok[3],str):
        def_type = pok[2]
        idef = type_index(def_type)
        iatt = type_index(att_type)
        if type_chart[iatt][idef] > 1:
            return True
        return False
    else: 
        def_type_1 = pok[2]
        def_type_2 = pok[3]
        idef1 = type_index(def_type_1)
        idef2 = type_index(def_type_2)
        iatt = type_index(att_type)
        if type_chart[iatt][idef1]*type_chart[iatt][idef2] > 1:
            return True
        return False
  
#debilidades por pokemon
weak_by_poke=[]

for p in data_list:
    weak=[]
    for t in pokemon_types:
        if weak_to_type(p,t):
            weak.append(t)
    weak_by_poke.append(weak)

#verdadero si no resiste al menos 1 tipo del movepool de 4
def not_resist_covg(pok, subs):
    if not isinstance(pok[3],str):
        def_type = pok[2]
        idef = type_index(def_type)
        for att_type in subs:
            iatt = type_index(att_type)
            if type_chart[iatt][idef] >= 1:
                return True
        return False
    else: 
        def_type_1 = pok[2]
        def_type_2 = pok[3]
        idef1 = type_index(def_type_1)
        idef2 = type_index(def_type_2)
        for att_type in subs:
            iatt = type_index(att_type)
            if type_chart[iatt][idef1]*type_chart[iatt][idef2] >= 1:
                return True
        return False

#verdadero si es superefectivo al menos 1 tipo del movepool de 4
def weak_covg(pok, subs):
    if not isinstance(pok[3],str):
        def_type = pok[2]
        idef = type_index(def_type)
        for att_type in subs:
            iatt = type_index(att_type)
            if type_chart[iatt][idef] > 1:
                return True
        return False
    else: 
        def_type_1 = pok[2]
        def_type_2 = pok[3]
        idef1 = type_index(def_type_1)
        idef2 = type_index(def_type_2)
        for att_type in subs:
            iatt = type_index(att_type)
            if type_chart[iatt][idef1]*type_chart[iatt][idef2] > 1:
                return True
        return False

#todos los posibles movesets de 4 tipos distintos
covg = find_subsets(s,4)

#todos los conjuntos de 4 tipos tal que al menos uno de ellos hace daño al menos neutral para cada pokemon
super_covg=[]
for c in covg:
    cont=0
    for p in data_list:
        if not not_resist_covg(p,c):
            break
        cont+=1
    if cont==1072:
        super_covg.append(list(c))
        
print(super_covg)


#todos los conjuntos de 4 tipos tal que al menos uno de ellos hace daño superefectivo para cada pokemon (no existe)
ultra_covg=[]
for c in covg:
    cont=0
    for p in data_list:
        if not weak_covg(p,c):
            break
        cont+=1
    if cont==1072:
        ultra_covg.append(list(c))
        
print(ultra_covg)

#para saber qué tipo sale más en super_covg
cont_type=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for ms in super_covg:
    for t in pokemon_types:
        if t in ms:
            cont_type[type_index(t)]+=1

for i in range(18):
    print(pokemon_types[i], cont_type[i])


#calcular todos los pokemon con exactamente k debilidades
num_deb = 1
i=0
for w in weak_by_poke:
    if len(w)==num_deb:
        print(data_list[i])
    i+=1
        
