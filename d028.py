# -*- coding: utf-8 -*-
"""d028

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I2BfVqgxLbfRMFeC9WhNxI0m6U-82IhA
"""

# Curso em Vídeo de Python - Professor Gustavo Guanabara
# Aluno: Anderson Costa

# Desafio 029: Escreva um programa que faça o computador pensar em
# um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

from random import randint

cpu = randint(0,5)
user = int(input('Tente acertar o número que estou pensando: '))

if user == cpu:
  print(f'\nParabéns, você venceu!!! O número que pensei foi o {cpu}.')
else:
  print(f'\nQue pena, você perdeu!!! O número que pensei foi o {cpu}.')