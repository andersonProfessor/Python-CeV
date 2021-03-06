# -*- coding: utf-8 -*-
"""d018

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wZyd1m53szG5nwNhythgPhxzJUUrR061
"""

# Curso em Vídeo de Python - Professor Gustavo Guanabara
# Aluno: Anderson Costa

# Desafio 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.

from math import sin, cos, tan, radians

theta = int(input('Insira um ângulo qualquer: '))
print(f'O seno de {theta}° é {sin(radians(theta)):.2f}.')
print(f'O cosseno de {theta}° é {cos(radians(theta)):.2f}.')
print(f'A tangente de {theta}° é {tan(radians(theta)):.2f}.')