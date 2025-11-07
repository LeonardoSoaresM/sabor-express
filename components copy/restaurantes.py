from .restaurante import Restaurante


class Restaurantes:
    def __init__(self, restaurantes_data):
        self._lista_de_restaurantes = self.obter_restaurantes(restaurantes_data)
    
    def obter_restaurantes(self, restaurantes_data):
        lista_de_restaurantes = []
        for restaurante in restaurantes_data["restaurants"]:
            lista_de_restaurantes.append(
                Restaurante(
                    nome=restaurante["name"],
                    categoria=restaurante["category"],
                    cardapio=restaurante["menu"],
                    avaliacoes=restaurante["ratings"]
                )
            )
        return lista_de_restaurantes