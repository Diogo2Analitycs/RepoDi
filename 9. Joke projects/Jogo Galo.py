# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:23:59 2020

@author: Diogo PC
# Jogo do galo, faltava aplicar uma forma de se quadrante já selecionado, escolher outro

"""

import random 

Tabuleiro = [0, 1, 2, 3, 4, 5, 6, 7, 8,]
t = Tabuleiro

def show():
    print (t[0],"|",t[1],"|",t[2])
    print ("---------")
    print (t[3],"|",t[4],"|",t[5])
    print ("---------")
    print (t[6],"|",t[7],"|",t[8])
show()
while True:
    

    pergunta= input("Seleciona um quadrante: ")
    pergunta=int(pergunta)
    
    if t[pergunta] != "x" and t[pergunta] != "0":
        t[pergunta] = "$"
        
        finding = True
        while finding:
            random.seed()
            adversario = random.randint(0,8)
        
            if t[adversario] != "o" and t[adversario] != "x":
                t[adversario] = "&"
                finding = False
        
    else:
        print("Quadrante já ocupado")

    show()
