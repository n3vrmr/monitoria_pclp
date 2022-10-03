#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:08:44 2022

@author: mac-prof
"""

n=True
while n:
    n=False
    print("Oi")
    
# Loop for

for i in range(0,6):
    print(i)


nome = ["Rafael", "Santana", "Izadora", "Gabriela"]
for item in nome:
    print(f"Olá, {item}!")
    
    
x = 7

# Blocos if


a = 0


if a > 0:
    print("Maior que zero")
else:
    print("?")

import random

def bingo(cartela:list,acertos:int):
    sorteios = 0
    correto = []
    while len(correto) < acertos:
        sorteado = random.sample(range(75),k=1)
        sorteios = sorteios + 1
        for numero in sorteado:
            sorteado.pop(sorteado.index(numero))
            if numero in cartela:
                correto.append(numero)
    print("Você riscou os números",correto)
    print(f"Você precisou de {sorteios} rodadaas para fazer isso.")
    return correto, sorteios

valores = [1, 7, 9, 19,
           23, 34, 31, 17,
           69, 42, 73, 60]
bingo(valores,3)
