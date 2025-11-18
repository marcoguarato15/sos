from datetime import datetime

class Nota():
    def __init__(self, titulo, demanda_id, prioridade_id, data_criacao):
        self.__titulo = titulo
        self.__demanda_id = demanda_id
        self.__prioridade_id = prioridade_id
        self.__data_criacao = datetime.now()

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
    def prioridade_id(self):
        return self.__prioridade_id
    
    @prioridade_id.setter
    def prioridade_id(self, prioridade_id):
        self.__prioridade_id = prioridade_id

    @property
    def data_criacao(self):
        return self.__data_criacao
    