import pytest
from components.avaliacao_restaurante import AvaliacaoRestaurante as Avaliacao

def test_init_avaliacao_restaurante_vazio():
    dados_vazios = {'average': 0, 'individual_ratings': []}
    
    # É assim que a classe é realmente inicializada
    avaliacao_container = Avaliacao(
        media=dados_vazios['average'], 
        avaliacoes_individuais=dados_vazios['individual_ratings']
    )
    
    assert avaliacao_container.media == 0
    assert avaliacao_container.avaliacoes_individuais == []

def test_init_avaliacao_restaurante_com_dados():
    dados_reais = {
        'average': 4.5, 
        'individual_ratings': [
            {'rating': 5}, 
            {'rating': 4}
        ]
    }
    
    avaliacao_container = Avaliacao(
        media=dados_reais['average'], 
        avaliacoes_individuais=dados_reais['individual_ratings']
    )
    
    assert avaliacao_container.media == 4.5
    assert len(avaliacao_container.avaliacoes_individuais) == 2
    assert avaliacao_container.avaliacoes_individuais[0]['rating'] == 5