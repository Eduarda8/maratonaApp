from model.pessoa import pessoa

class funcionario(pessoa):

    def __init__(self,nome):
        super(funcionario, self).__init__(nome)
