# -*- coding: utf-8 -*-
"""d021

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ekFGWkmTdSYZdPxufjXjhWlBR4w2gx92
"""

# Curso em Vídeo de Python - Professor Gustavo Guanabara
# Aluno: Anderson Costa

# Desafio 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#from playsound import playsound
#playsound('sonic.mp3')

from pygame import mixer
 
mixer.init() 
mixer.music.load("sonic.mp3") 
mixer.music.set_volume(0.7) 
mixer.music.play() 
while True: 
      
    print("Press 'p' to pause, 'r' to resume") 
    print("Press 'e' to exit the program") 
    query = input("  ") 
      
    if query == 'p': 
        mixer.music.pause()      
    elif query == 'r': 
        mixer.music.unpause() 
    elif query == 'e': 
        mixer.music.stop() 
        break