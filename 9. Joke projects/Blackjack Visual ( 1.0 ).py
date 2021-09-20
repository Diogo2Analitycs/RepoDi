# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:55:38 2019

@author: Diogo PC
"""
import os
import random
from random import randint

#Configuração inicial
baralho = ["A","2","3","4","5","6","7","8","9","10","V","D","R"]
naipe = ["Copas" ,"Paus", "Espadas" ,"Ouros"]
mao = []

for b in baralho:
    for n in naipe:
        mao.append(b + " of " + n )
print(mao)






 
