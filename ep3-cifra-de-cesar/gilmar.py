#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Gilmar S. Santos <gilmar.pythonman@outlook.com>

"""
Importa módulo string e argparse para criptografar e descriptografar texto
Referências:
    - https://docs.python.org/2/library/string.html
    - https://docs.python.org/2/library/argparse.html
"""

# Limita o que será importado ao usar "from gilmar import *" em outro arquivo
# ou no modo iterativo (digitando "python" neste diretório no terminal)
__all__ = ("encrypt", "decrypt",)

import string

pythonman = """
  _ __  _  _ | |_ | |_   ___  _ _   _ __   __ _  _ _
 | '_ \| || ||  _|| ' \ / _ \| ' \ | '  \ / _` || ' \.
 | .__/ \_, | \__||_||_|\___/|_||_||_|_|_|\__,_||_||_|
 |_|    |__/
"""


def encrypt(text):
    """
        Criptografa a string informada no param.
        Exempo de uso:
            print encrypt("teste")
            nymny
    """
    return __passwd_make(text)


def decrypt(text):
    """
    Descriptografa a string informada no param.
    Exempo de uso:
        print decrypt("nymny")
        teste
    """
    return __passwd_make(text, False)


def __passwd_make(text, encrypt=True):
    BASE_KEY = "UVWXYZABCDEFGHIJKLMNOPQRST4567890123"
    BASE_CHAR = string.ascii_uppercase + string.digits

    if encrypt:
        keys, chars = BASE_KEY, BASE_CHAR
    else:
        keys, chars = BASE_CHAR, BASE_KEY

    pwd = ""
    for i in range(len(text)):
        try:
            l = chars.index(text[i].upper())
            pwd += keys[l] if text[i].isupper() else keys[l].lower()
        except Exception:
            pwd += text[i]

    return pwd


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Cifra de Cesar")

    parser.add_argument("-c", "--encrypt",
                        help="Criptografa o texto informado.",
                        action="store_true")

    parser.add_argument("-d", "--decrypt",
                        help="Descriptografa o texto informado.",
                        action="store_true")

    args = parser.parse_args()

    if not args.encrypt and not args.decrypt:
        print pythonman
        parser.print_help()
        parser.exit()

    try:
        complement = "des" if args.decrypt else ""
        message = "Entre com o texto para {0}criptografia: ".format(complement)
        text = str(raw_input(message))

    except KeyboardInterrupt, e:
        print "\nObrigado por usar nossos scripts."
        parser.exit()

    except ValueError, e:
        parser.print_help()
        parser.exit()

    if args.encrypt:
        passwd = encrypt(text).center(54)
    else:
        passwd = decrypt(text).center(54)

    print pythonman, passwd
    print
