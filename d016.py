# -*- coding: utf-8 -*-
"""d016

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kKHZ4XdO6Otq_WVPwSNcXMhvvCV0J09T
"""

# Curso em Vídeo de Python - Professor Gustavo Guanabara
# Aluno: Anderson Costa

# Desafio 016: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import floor

num = float(input('Digite um número real qualquer: '))
print(f'A porção inteira desse número é {int(floor(num))}.')