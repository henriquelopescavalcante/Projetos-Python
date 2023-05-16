import pytest
from wallet import wallet, insulfficientamount

@pytest.fixture
def carteira():
    return Wallet(10)


def test_saldo_inicial_sem_parametro():
    carteira = wallet()
    assert carteira.saldo == 0


def test_saldo_inicial_com_parametro(carteira):
    assert carteira.saldo == 10

def test_adiciona_saldo(carteira):
    carteira.add_cash(10)
    assert carteira.saldo == 20

# :: chamar só um test com o nome do que esta no def.
# @pytest.mark.slow  testes lentos
def test_retirar_da_carteira_com_saldo(carteira):
    carteira.spend_cash(10)
    assert carteira.saldo == 0

def test_retirar_da_carteira_com_saldo_suficiente(carteira):
    with pytest.raises(insulfficientamount):
    carteira.spend_cash(20)

def test_retira_da_carteira_parte_do_saldo(carteira):
    carteira.spend_cash(5)
    assert carteira.saldo == 5
