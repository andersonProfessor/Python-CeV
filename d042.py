# -*- coding: utf-8 -*-
"""d042

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GUAZ0EPAuw9YK3lK3gdSszNJmhlsSjC9
"""

# Curso em Vídeo de Python - Professor Gustavo Guanabara
# Aluno: Anderson Costa

# Desafio 042: Refaça o d035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# - Equilátero: todos os lados iguais.
# - Isósceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.

r1 = float(input('Medida da RETA 1: '))
r2 = float(input('Medida da RETA 2: '))
r3 = float(input('Medida da RETA 3: '))

if abs(r2 - r3) < r1 < (r2 + r3) and abs(r1 - r3) < r2 < (r1 + r3) and abs(r1 - r2) < r3 < (r1 + r2):
  if (r1 == r2) and (r2 == r3):
    print('\nO triângulo é EQUILÁTERO!')
  elif (r1 != r2) and (r1 != r3) and (r2 != r3):
    print('\nO triângulo é ESCALENO!')
  else:
    print('\nO triângulo é ISÓSCELES!')
else:
  print('\nAs retas NÃO podem formar um triângulo!')