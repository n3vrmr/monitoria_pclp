# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:46:40 2022

@author: Nevermore
"""

# Variáveis
## Como declarar uma variável em Python?



## Quais são os tipos de objetos?

a = 'Calvin'
b = 7
c = 273.15
d = True
e = input("Quanto é b*3? ")

print(type(e))

## Mude o tipo do objeto 'e'.



# f-string

print(f"{a} tem {b} anos de idade.")

## Crie quatro listas com 5 variáveis cada.
### Objetos dos mesmos tipos em cada lista.

lista_1 = [a, 'Álvaro', 'Matheus', 'Victória', 'Cebolinha']
lista_2 = [b, 33, 23, 25, 8]
lista_3 = [c, 373.15, 233.15, 298.15, 303.15]
lista_4 = ['Haroldo', 'Xerxes', 'Luna', 'Ana', 'Cascão']

## Como fazer referência a um elemento de uma lista?
### E vários elementos?



## Crie um diconário com 4 elementos.

calvin = {'nome':'Calvin',
          'idade':7,
          'temp_preferida':273.15,
          'melhor_amigo':'Haroldo'}

## Como encontrar as chaves de um dicionário?



## Como fazer referência a um valor de um dicionário?



## Crie um dicionário com as listas que você criou.

houiass = {'nome':lista_1,
            'idade':lista_2,
            'temp_preferida':lista_3}


# SPOILER
import pandas as pd

df = pd.DataFrame(houiass)

# Controle de fluxo
## O que é controle de fluxo?



## Laços for e as funções range() e enumerate()
### Crie um laço for para dar print em todos os elementos de uma lista.
### Crie um outro laço for para dar print nos índices também.



### Função items() para dicionários



## Laços if
### Crie um laço if com condições referentes aos objetos a, b, c e d.



## Crie um laço if dentro de um laço for.



def main():
    print('Hello, world')
    return

if __name__ == '__main__':
    main()
