from tests.fixtures import sobremesa_fixture

def teste_aplicar_desconto_sobremesa(sobremesa_fixture):
    sobremesa = sobremesa_fixture
    sobremesa.aplicar_desconto()

    assert sobremesa._preco == 85