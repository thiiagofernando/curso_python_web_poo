from modelos.restaurante import  Restaurante
from modelos.cardapio.bebida import  Bebida
from modelos.cardapio.prato import  Prato

restaurante_praca = Restaurante('Praca','Gourmet')
bebida_suco = Bebida('Suco Laranja',5.0,'Grande')
prato_lasanha = Prato('Lasanha',15.0,'Com muito queijo')




def main():
    print(bebida_suco)
    print(prato_lasanha)
if __name__ == '__main__':
    main()