# -*- coding: utf-8 -*-
"""d020

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lz6S68sg5rczPeID0oPqpf7RoZzvA1bz
"""

# Curso em Vídeo de Python - Professor Gustavo Guanabara
# Aluno: Anderson Costa

# Desafio 020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

p1 = input('Primeiro Aluno: ')
p2 = input('Segundo Aluno: ')
p3 = input('Terceiro Aluno: ')
p4 = input('Quarto Aluno: ')

lista = [p1, p2, p3, p4]
shuffle(lista)

print(f'\nA ordem de apresentação do trabalho é: {lista}.')