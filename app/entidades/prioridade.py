class Prioridade():
    def __init__(self, nome, id_prioridade):
        self.__nome = nome
        self.__id_prioridade = id_prioridade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def id_prioridade(self):
        return self.__id_prioridade
    
    @id_prioridade.setter
    def id_prioridade(self, id_prioridade):
        self.__id_prioridade = id_prioridade