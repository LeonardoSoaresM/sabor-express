import json

from .restaurantes import Restaurantes


class SaborExpress:
    def __init__(self):
        self._restaurantes = None

    def exibir_nome_do_programa(self):
        ''' Exibe o nome do programa '''
        print("""
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """)

    def obter_restaurantes(self):
        with open("data/restaurants_db.json") as file:
            restaurants_data = json.load(file)

        restaurantes = Restaurantes(restaurants_data)

        self._restaurantes = restaurantes

    def escolher_restaurante(self, restaurante_escolhido_index):
        restaurante_escolhido = self._restaurantes._lista_de_restaurantes[restaurante_escolhido_index - 1]

        return restaurante_escolhido

    def escolher_pedido(self, restaurante_escolhido, pedido_escolhido_index):
    
        return restaurante_escolhido._cardapio[pedido_escolhido_index - 1]

    def calcular_preco(self, pedido_escolhido, tem_desconto):
        if tem_desconto == "S":
            pedido_escolhido.aplicar_desconto()

        print(f"O pedido ficou por {pedido_escolhido._preco:.2f}")

    def avaliar_pedido(self, idx):
        
            nota_avaliacao = int(input("Nota (1 a 5):"))
            descricao_avaliacao = input("Comentário:")

            self._restaurantes._lista_de_restaurantes[idx]._avaliacoes.avaliacoes_individuais.append({
                "rating": nota_avaliacao,
                "description": descricao_avaliacao
            })

            self._restaurantes._lista_de_restaurantes[idx].calcular_media_avaliacoes

            # save json
            nova_avaliacao = {
                "average": self._restaurantes._lista_de_restaurantes[idx]._avaliacoes.media,
                "individual_ratings": self._restaurantes._lista_de_restaurantes[idx]._avaliacoes.avaliacoes_individuais,
            }

            with open("nova_avaliacao.json", "w", encoding="utf-8") as file:
                json.dump({f"{self._restaurantes._lista_de_restaurantes[idx]._nome}": nova_avaliacao}, file, ensure_ascii=False, indent=4)


            print("\nObrigado pela avaliação!")

        

    def iniciar_interface_de_pedidos(self):
        # Mostra lista de restaurantes e obtém o escolhido
        print("Digite o número do restaurante no qual deseja fazer o pedido.")
        
        for idx, restaurante in enumerate(self._restaurantes._lista_de_restaurantes):
            print(f"{idx + 1}" + f" - {restaurante._nome}" )

        restaurante_escolhido_index = int(input("Restaurante escolhido: "))
        
        restaurante_escolhido = self.escolher_restaurante(restaurante_escolhido_index)

        # Mostra lista de pedidos do restaurante e obtém o escolhido
        print("\nDigite o número do item que deseja pedir.")
        restaurante_escolhido.exibir_cardapio
        pedido_escolhido_index = int(input("Pedido escolhido: "))

        pedido_escolhido = self.escolher_pedido(restaurante_escolhido, pedido_escolhido_index)

        # Calcula o preço do pedido após verificar se tem desconto ou não
        tem_desconto = input("Você tem cupom de desconto? (S/N)")

        self.calcular_preco(pedido_escolhido, tem_desconto)

        # Permite que o usuário faça uma avaliação
        deseja_avaliar = input("Deseja fazer uma avaliação? (S/N)")

        if deseja_avaliar == "S":
            self.avaliar_pedido(restaurante_escolhido_index)

        print("\nPedido finalizado.")