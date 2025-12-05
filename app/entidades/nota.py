from datetime import datetime

class Nota():
    def __init__(self, titulo, demanda_id, ativo):
        self.__titulo = titulo
        self.__demanda_id = demanda_id
        self.__data_criacao = datetime.now()
        self.__ativo = ativo

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def demanda_id(self):
        return self.__demanda_id
    
    @demanda_id.setter
    def demanda_id(self, demanda_id):
        self.__demanda_id = demanda_id

    @property
    def ativo(self):
        return self.__ativo
    
    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo

    @property
    def data_criacao(self):
        return self.__data_criacao
    