#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#guession_game.py - Jogo de adivinhação

"""
Importa módulo random e sorteia
um número inteiro entre 1 e 100
"""

import random

number = random.randint( 1 , 100 )
choice = 0
attempts = 0

while choice != number :
	choice = input( "Escolha um número entre 1 e 100\n" )
	attempts += 1

	if choice < number:
		print "O número", choice, "é menor que o sorteado."
	elif choice > number :
		print "O número", choice, "é maior que o sorteado."

print "Parabéns! Você acertou com", attempts, "tentativas."
