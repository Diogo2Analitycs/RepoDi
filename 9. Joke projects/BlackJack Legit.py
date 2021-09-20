# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:29:24 2020

@author: Diogo PC
"""

#Tentativa de Blackjack, ainda por fazer 

import os
import random

#Configuração inicial
baralho = ["A","2","3","4","5","6","7","8","9","10","V","D","R"]
mao = []

#Perguntar se inicia o jogo
def start_menu():

  print ("  ")
  linguagem = input("[P]ortugues or [E]nglish ?\n")
  if linguagem == "p" or linguagem == "P":
    print("nice meu puto")
  
  elif linguagem == "e" or linguagem == "E":
    print(" ")
    print("Achas mesmo que perdi tempo a fazer a versão em ingles?\nDeves pensar que tenho a tua vida cabrão, eu chego a casa e tenho de fazer o jantar,  achas mesmo que ia programar esta merda em ingles?! \n Epah olha, so não te meto um virus no pc porque o meu uber eats chegou, senão estavas na merda")
  
  else:
    print(" ")
    print("Não caralho, é entre Portugues ou Ingles")
    start_menu()

start_menu()
#print(random.choice(mao))
#Se y, começa o jogo

#Se n, "fechar" 

#Se conseguir, fazer com dinheiro mesmo

#Ingles ou Portugues

#Perguntar se inicia o jogo
inicio = input("Vamos Jogar BlackJack? y/n?\n")

#quantos baralhos

#Distribuir cartas para jogardor e dizer valor

#Distribuir cartas para dealer e dizer valor

#Perguntar ao jogador se HIT ou PASS

#Dar carta a jogardor e dizer valor

#Perguntar ao jogador se HIT ou PASS

#Distribuir cartas a jogar e dealer

# GANHOU OU PERDEU 

#DE NOVO?