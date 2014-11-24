# -*- encoding: utf-8 -*-

class ExchangeCalculator(object):
    """Responsible for user change the calculation."""
    
    def __init__(self, available_paper, available_coins):
        self.available_paper = available_paper
        self.available_coins = available_coins

    def calculate(self,value, received):
        if value > received:
            raise Exception(
                "The received value may not be larger than the initial value."
            )

        change_value = float(received) - float(value)

        return self._change_for(change_value)

    def _change_for(self, change_value):
        if change_value > 1 and len(self.available_paper) > 0:
            for p in reversed(self.available_paper):
                if change_value >= p:
                    n = int(change_value/p)
                    r = change_value - p * n
                    print ": %s nota(s) de R$ %s." % (n, p)
                    change_value = r

            if change_value > 0:
                change_value *= 100
                print change_value
                for p in reversed(self.available_coins):
                    if change_value >= p:
                        n = int(change_value/p)
                        r = change_value - p * n
                        print ": %s moedas(s) de %s centavos." % (n, p)
                        change_value = r
