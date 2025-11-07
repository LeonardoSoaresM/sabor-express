from components.sabor_express import SaborExpress

def main():
    sabor_express = SaborExpress()

    sabor_express.exibir_nome_do_programa()
    sabor_express.obter_restaurantes()
    sabor_express.iniciar_interface_de_pedidos()

if __name__ == '__main__':
    main()