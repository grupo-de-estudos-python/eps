#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Gilmar S. Santos <gilmar.pythonman@outlook.com>

import sys
import core

def get_change_formated_for(total, received_value):
    """
        Calcula o valor e as respectivas cédulas de troco
        Exempo de uso:
            print calculate_change(55.60, 60)
                2 cédulas de 2 reais.
                1 moeda de 25 centavos.
                1 moeda de 10 centavos.
                1 moeda de 5 centavos.
    """

    available_paper = [1,2,5,10,20,50,100]
    available_coins = [1,5,10,25,50]

    exchanger = core.ExchangeCalculator(available_paper,available_coins)
    change_values = exchanger.calculate(total, received_value)
    # for k, v in change_values.iteritems():
    #     print k, v

if __name__ == "__main__":
    try:
        total = float(raw_input("Entre com o valor inicial:"))
        received_value = float(raw_input("Entre com o valor recebido:"))

        get_change_formated_for(total, received_value)

    except KeyboardInterrupt, e:
        print "\nBye"
        sys.exit()

    except ValueError, e:
        print e
        sys.exit()