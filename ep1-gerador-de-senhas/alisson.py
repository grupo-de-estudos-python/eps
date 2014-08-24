#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Alisson R. Perez <alissonperez@outlook.com>

"""
Gerador de senhas aleatórias
Alisson R. Perez <alissonperez@outlook.com>
"""


# Limita o que será importado ao usar "from alisson import *" em outro arquivo
# ou no modo iterativo (digitando "python" neste diretório no terminal)
__all__ = ("rand_passwords",)


def rand_passwords(size, special=""):
    """
    Gera 10 opções de senha com o tamanho informado
    e incluindo os caracteres especiais também informados.
    """

    import random

    default = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" + special

    # Remove os caracteres duplicados com a função set()
    # https://docs.python.org/2/library/stdtypes.html#set
    default = str("".join(set(default)))

    passwords = []

    num = 10
    for i in range(num):
        password = []

        for s in range(size):
            choice = random.choice(default)
            if random.randint(0, 1) == 0:
                choice = choice.lower()

            password.append(choice)

        passwords.append("".join(password))

    return passwords


# O trecho a seguir é executado apenas quando executamos o
# script na mao. Por exemplo:
#
# $ python alisson.py
#
# OU
#
# $ ./alisson.py
#
# No caso de importarmos este arquivo em outro, este trecho não é executado.
# Exemplo, no diretório deste arquivo:
#
# $ python
# >>> import alisson
# >>> print alisson.rand_passwords(10) # aqui é chamada a função
# ...                                  # acima, neste arquivo
#
# OU
#
# $ python
# >>> from alisson import *
# >>> print rand_passwords(10) # Mesmo comportamento, porém recomenda-se a
#                              # forma acima para não
#                              # conflitar com nomes locais
if __name__ == "__main__":
    try:
        size = int(raw_input("Entre com o comprimento da senha: "))

        special = str(raw_input("Entre com caracteres opcionais para inclusão "
                                "nas senhas. (Opcional, aperte Enter para "
                                "pular esta etapa):"))

        for password in rand_passwords(size, special):
            print password

    except KeyboardInterrupt, e:
        print ""
        print "Bye..."

    except ValueError, e:
        print ""
        print "Valor incorreto"
