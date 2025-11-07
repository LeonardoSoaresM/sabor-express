from components.cardapio.sobremesa import Sobremesa
from components.restaurantes import Restaurantes
from components.sabor_express import SaborExpress
import pytest

@pytest.fixture
def sabor_express_object_fixture():
    sabor_express_mock = SaborExpress()
    sabor_express_mock._restaurantes = Restaurantes({
            "restaurants": [
                {
                    "name": "restaurante 1",
                    "category": "tradicional",
                    "menu": [
                        {
                            "Item": "Item 1",
                            "Price": 5,
                            "Description": "An item 1"
                        },
                        {
                            "Item": "Item 2",
                            "Price": 10,
                            "Description": "An item 2"
                        },
                        {
                            "Item": "Item 1",
                            "Price": 6,
                            "Description": "An item 3"
                        }
                    ],
                    "ratings": {
                        "average": 3,
                        "individual_ratings": [
                            {
                                "rating": 3,
                                "description": "Don't like it that much"
                            }
                        ]
                    }
                },
                {
                    "name": "restaurante 2",
                    "category": "tradicional",
                    "menu": [
                        {
                            "Item": "Item 1",
                            "Price": 5,
                            "Description": "An item 1"
                        },
                        {
                            "Item": "Item 2",
                            "Price": 10,
                            "Description": "An item 2"
                        },
                        {
                            "Item": "Item 1",
                            "Price": 6,
                            "Description": "An item 3"
                        }
                    ],
                    "ratings": {
                        "average": 3,
                        "individual_ratings": [
                            {
                                "rating": 3,
                                "description": "Don't like it that much"
                            }
                        ]
                    }
                }
            ]
        })
    
    return sabor_express_mock

@pytest.fixture
def sobremesa_fixture():
    return Sobremesa(
        nome="Sorvete",
        preco=100,
        tipo="Gelados",
        tamanho="500ml"
    )