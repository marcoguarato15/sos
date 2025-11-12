class Tipo():
    def __init__(self, nome, id_tipo):
        self.__nome = nome
        self.__id_tipo = id_tipo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def id_tipo(self):
        return self.__id_tipo
    
    @id_tipo.setter
    def id_tipo(self, id_tipo):
        self.__id_tipo = id_tipo
