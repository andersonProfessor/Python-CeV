# -*- coding: utf-8 -*-
"""d031

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cYAMjh0SAxtDeFwSnZ1aTCjDUzzNv6BJ
"""

# Curso em Vídeo de Python - Professor Gustavo Guanabara
# Aluno: Anderson Costa

# Desafio 031: Desenvolva um programa que pergunte a distância de uma viagem
# em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens até
# 200 Km e R$ 0,45 para viagens mais longas.

dist = float(input('Distância da Viagem (Km): '))

if dist >= 200.0:
  print(f'\nO preço da viagem é R$ {dist*0.50:.2f}.')
else:
  print(f'\nO preço da viagem é R$ {dist*0.45:.2f}.')