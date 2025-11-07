from .item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)