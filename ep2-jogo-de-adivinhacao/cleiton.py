#!usr/bin/env python
# -*- encoding: utf-8 -*-

import random
random.seed() # inicializa o contador
s = random.randint(1,100) #gera numero randomico inteiro
n = 0
t = 0
while True:
	try:
		n = int(raw_input("Digite o numero de 1 a 100: " ))
		t = t + 1
		if n == s:
			print "Resultado CORRETO, valor sorteado %d" % s
			print "Parabens voce acertou o resultado em %d tentativas" % t
			break
		elif s > n :
			print "Sorteado numero MAIOR, tente novamente"
		elif s < n :
			print "Sorteado numero MENOR, tente novamente"
	except ValueError:
		print "Favor digitar um numero inteiro valido de 0 a 100."