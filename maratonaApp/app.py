from maratona import maratona
from cliente import cliente
from funcionario import funcionario



def main():

    funcionario= funcionario("josé")
    cliente = cliente("maria")

    maratona= maratona()
    maratona.correr(cliente)
    maratona.correr(funcionario)

if __name__=="__main__":
    main()
