from model.pessoa import pessoa

class cliente(pessoa):

    def __init__(self,nome):
        super(cliente, self).__init__(nome)

    def pagar(self):
        print("Pagando como um cliente")
