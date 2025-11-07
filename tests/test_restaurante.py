import pytest
from components.restaurante import Restaurante
from components.cardapio.sobremesa import Sobremesa

@pytest.fixture
def restaurante_vazio():
    return Restaurante(
        nome="Cantina Vazia", 
        categoria="Testes", 
        cardapio=[], 
        avaliacoes={'average': 0, 'individual_ratings': []}
    )

@pytest.fixture
def restaurante_com_avaliacoes():
    avaliacoes_data = {
        'average': 0, # A média inicial é 0, mas o método calcular_media deve corrigir
        'individual_ratings': [
            {'rating': 5},
            {'rating': 3}
        ]
    }
    return Restaurante(
        nome="Restaurante Avaliado", 
        categoria="Testes", 
        cardapio=[],
        avaliacoes=avaliacoes_data
    )

@pytest.fixture
def item_sobremesa():
    try:
        return Sobremesa(nome="Pudim", preco=10.0, tipo="Doce", tamanho="Pequeno")
    except TypeError:
        return Sobremesa(nome="Pudim", preco=10.0)

def test_media_avaliacoes_sem_avaliacoes(restaurante_vazio):
    assert restaurante_vazio._avaliacoes.media == 0

def test_adicionar_no_cardapio(restaurante_vazio, item_sobremesa):
    restaurante_vazio.adicionar_no_cardapio(item_sobremesa)
    assert len(restaurante_vazio._cardapio) == 1
    
    # CORREÇÃO AQUI: O atributo é '_nome' (privado), não 'nome'
    assert restaurante_vazio._cardapio[0]._nome == "Pudim"

def test_calcular_media_avaliacoes(restaurante_com_avaliacoes):
    assert restaurante_com_avaliacoes._avaliacoes.media == 0
    
    restaurante_com_avaliacoes.calcular_media_avaliacoes()
    
    assert restaurante_com_avaliacoes._avaliacoes.media == 4.0