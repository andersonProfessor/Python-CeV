# -*- coding: utf-8 -*-
"""d015

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KwGU9G5injMYDtz8TZbYbEcnR4gxQGbr
"""

# Curso em Vídeo de Python - Professor Gustavo Guanabara
# Aluno: Anderson Costa

# Desafio 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60/dia e R$ 0,15/Km.

dias = int(input('Por quantos dias o carro foi alugado? '))
Km = float(input('Quantos quilômetros foram percorridos? '))
preço = 60*dias + 0.15*Km
print(f'O preço total do aluguel é R$ {preço:.2f}.')