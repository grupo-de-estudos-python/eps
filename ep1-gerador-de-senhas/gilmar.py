#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Gilmar S. Santos <gilmar.pythonman@outlook.com>

"""
Importa módulo random, sys e string para gerar
senhas aleatórias.
Referências:
    - https://docs.python.org/3/library/string.html
    - https://docs.python.org/3/library/random.html
    - https://docs.python.org/3/library/sys.html
"""

import string
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

Obrigado por utilizar nossos scripts!
"""

answer = """
                .-'''-.
              ./ .===. \.
               \/ 6 6 \/
               ( \___/ )
 __________ooo__\_____/_______________
|                                     |
| Senha gerada com sucesso! Tome nota:|
| ----------------------------------- |
| {0} |
| ----------------------------------- |
|_______________________ooo___________|
                |  |  |
                |_ | _|
                |  |  |
                |__|__|
                /-'Y'-\.
               (__/ \__)
"""

try:
    # Obter o comprimento da senha e os caracteres adicionais
    size = int(raw_input("Entre com o comprimento da senha:"))
    special_chars = raw_input(
        "Entre com caracteres opcionais para inclusão nas senhas."
        "(Opcional, aperte Enter para pular esta etapa):")

except KeyboardInterrupt, e:
    print pythonman
    sys.exit(0)

except ValueError, e:
    print("O comprimento da senha é obrigatório e deve ser númerico.")
    sys.exit(0)


def generate_password(length, extra_chars=''):
    chars = string.ascii_letters + string.ascii_uppercase + string.digits

    pwd = ""
    for n in range(int(length)):
        pwd += str(random.choice(chars + extra_chars))

    return pwd

pwd = generate_password(size, str(special_chars))

if size > 35:
    hr = "-" * size
    print ""
    print "Senha gerada com sucesso:".center(size)
    print hr
    print pwd
    print hr
    print pythonman
else:
    print answer.format(pwd.center(35))
