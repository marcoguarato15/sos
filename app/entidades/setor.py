from datetime import datetime

class Setor():
    def __init__(self, nome, gestor_id, ativo,membros=None):
        self.__nome = nome
        self.__gestor_id = gestor_id
        self.__membros = membros
        self.__ativo = ativo
        self.__data_criacao = datetime.now()

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def gestor_id(self):
        return self.__gestor_id
    
    @gestor_id.setter
    def gestor_id(self, gestor_id):
        self.__gestor_id = gestor_id

    @property
    def membros(self):
        return self.__membros
    
    @membros.setter
    def membros(self, membros):
        self.__membros = membros

    @property
    def data_criacao(self):
        return self.__data_criacao
    
    @property
    def ativo(self):
        return self.__ativo
    
    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo