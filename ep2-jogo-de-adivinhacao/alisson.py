#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Alisson R. Perez <alissonperez@outlook.com>

import random
import sys

# Obter o range inicial, caso não informado via linha de comando
try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
except Exception, e:
    # Usa-se o parenteses para dar quebra de linha
    # Sem quebrar a sintaxe e manter assim as 80 linhas
    print ("Foi usado uma faixa padrão, caso queira informe na linha"
           "de comando a faixa desejada.")

    print "Ex: '{} 0 500'".format(__file__)
    start = 0
    end = 100

num = random.randint(start, end)

print "Número gerado..."

choice = None
attemps = 0

while choice != num:
    try:
        choice = raw_input(
            "Entre com um número entre {} e {}: ".format(start, end))

        choice = int(choice)
        attemps += 1

        if choice < num:
            print "^ MAIOR. Tente novamente"
        elif choice > num:
            print "V MENOR. Tente novamente"
        elif choice == num:
            print "Parabéns, você acertou em {} tentativas!".format(attemps)
    except ValueError, e:
        print "Valor incorreto, tente novamente."
        continue
    except KeyboardInterrupt, e:
        print ""
        print "Bye!"
        break
