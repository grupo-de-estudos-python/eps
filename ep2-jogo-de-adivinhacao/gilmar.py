#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Gilmar S. Santos <gilmar.pythonman@outlook.com>

"""
Importa módulo random e sorteia
um número inteiro entre 1 e 100
"""

import random
import sys

pythonman = """

       ***********
    ***** ***********
 ** ****** *** ********
****  ******  ** *******
***     ******    ******
***                 *  **
 *|/------  -------\ ** *
  |       |=|       :===**
   |  O  |   | O   |  }|*
    |---- |   ----  |  |*
    |    |__        |\/
    |              |
     \   -----    |
      \          |
       -_ _ __- /
"""

start = 1
end = 100

number = random.randint(start, end)

choice = None
attempts = 0
while choice != number:
    try:
        attempts += 1
        choice = raw_input(
            "Escolha um número entre {0} e {1}\n".format(start, end))

        if int(choice) < number:
            print "O número", choice, "é menor que o sorteado."
        elif int(choice) > number:
            print "O número", choice, "é maior que o sorteado."
        elif int(choice) == number:
            print "Parabéns! Você acertou com", attempts, "tentativas."
            break
    except ValueError, e:
        print("Valor inválido, digite um número entre {0} e {1}."
              .format(start, end))
        continue
    except KeyboardInterrupt, e:
        print pythonman
        print "Bye bye!".center(22)
        print ""
        sys.exit(0)
