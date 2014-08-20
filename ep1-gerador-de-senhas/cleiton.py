#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Cleiton Melo cleiton.melo@gmail.com

import random

texto = "Entre com a quantidade de caracteres da senha. Minimo 8:"
tamanho = None

sUpper = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
sLower = 'abcdefghijklmnopqrstuvxwyz'
sNumeric = '01234567890'
sSpecial = ''

try:
    tamanho = int(raw_input(texto))
    # Verificando a quantidade minima de caracteres para a senha
    if tamanho < 8:
        raise
    # Verificando os caracteres para a senha
    sSpecial = raw_input("Favor selecionar caracteres especiais (Opcional): ")

    # Montando a String para pesquisa de caracteres
    sChars = sUpper + sLower + sNumeric + sSpecial

    # Loop para gerar senhas aleartórias
    contador = 0
    while contador <= 8:
        contador = contador + 1
        senha = ''
        for i in range(0, tamanho):
            senha += random.choice(sChars)
        print senha
except ValueError, e:
    print "Favor selecionar um valor inteiro valido"
except KeyboardInterrupt, e:
    print "Processo interrompido !"
except:
    print "Favor selecionar o minimo de caracteres de 8"
