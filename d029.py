# -*- coding: utf-8 -*-
"""d029

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VdgVeSE2viYwNQFhN1_49xTZB85dKqid
"""

# Curso em Vídeo de Python - Professor Gustavo Guanabara
# Aluno: Anderson Costa

# Desafio 029: Escreva um programa que leia a velocidade de um carro. Se ele
# ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado. A multa
# vai custar R$ 7,00 por cada Km acima do limite.

vel = float(input('Velocidade do Veículo: '))

if vel >= 80.0:
  print(f'\nVelocidade acima da permitida!!! Você foi multado em R$ {(vel-80)*7:.2f}.')
else:
  print(f'\nDirija com cuidado!!!')