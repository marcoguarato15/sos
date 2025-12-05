class PrioridadeTarefa():
    def __init__(self, nome, num_prioridade):
        self.__nome = nome
        self.__num_prioridade = num_prioridade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def num_prioridade(self):
        return self.__num_prioridade

    @num_prioridade.setter
    def num_prioridade(self, num_prioridade):
        self.__num_prioridade = num_prioridade