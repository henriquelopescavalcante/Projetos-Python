class insulfficientamount(Exception)
    pass
class wallet(object):
    
    def __init__(self, quantidade_inicial=0):
        self.saldo = quantidade_inicial

    def spend_cash(self, quantidade):
        if self.saldo < quantidade:
            raise insulfficientamount(f"nao ha o suficiente disponivel para gastar {quantidade}")
        self.saldo -= quantidade

    def add_cash(self, quantidade):
        self.saldo += quantidade
              

 