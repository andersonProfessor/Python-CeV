# -*- coding: utf-8 -*-
"""d034

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_QBm2lGheGvCYVBoqBUieEwbjDC6_tEy
"""

# Curso em Vídeo de Python - Professor Gustavo Guanabara
# Aluno: Anderson Costa

# Desafio 034: Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento.
# Para salários superiores a R$ 1250,00: Calcule um aumento de 10%.
# Para os inferiores ou iguais: Calcule um aumento de 15%.

sal = float(input('Informe seu salário: R$ '))

if sal > 1250.0:
  print(f'\nCom o reajuste de 10%, você terá um aumento de R$ {sal*0.10:.2f}, passando a receber R$ {sal + sal*0.10:.2f}')
else:
  print(f'\nCom o reajuste de 15%, você terá um aumento de R$ {sal*0.15:.2f}, passando a receber R$ {sal + sal*0.15:.2f}')