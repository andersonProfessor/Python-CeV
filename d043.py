# -*- coding: utf-8 -*-
"""d043

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HxdcUsahDhsxptQMtl0kNn3My30DoCqx
"""

# Curso em Vídeo de Python - Professor Gustavo Guanabara
# Aluno: Anderson Costa

# Desafio 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso Ideal
# - De 25 até 30: Sobrepeso
# - De 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

w = float(input('Insira seu peso(Kg): '))
h = float(input('Insira sua altura(m): '))

IMC = w/(h**2)

print(f'\nPara uma altura de {h:.2f}m e um peso de {w:.1f}Kg, seu IMC é {IMC:.1f}')

if IMC <= 18.5:
  print('\nVocê está abaixo do peso! Precisa comer mais!!!')
elif IMC > 18.5 and IMC <= 25:
  print('\nVocê está com o peso ideal! Parabéns, mantenha uma vida saudável!!!')
elif IMC > 25 and IMC <= 30:
  print('\nVocê está com sobrepeso! Tome cuidado para não perder o controle!!!')
elif IMC > 30 and IMC <= 40:
  print('\nVocê está obeso! Hora de reduzir a batata-frita já!!!')
else:
  print('\nProcure um médico urgentemente!!! Você está com obesidade mórbida!!!')