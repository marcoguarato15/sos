from datetime import datetime

class Tarefa():
    def __init__(self, titulo, prioridade_tarefa_id, status_tarefa_id, tempo_gasto_total, data_conclusao):
        self.__titulo = titulo
        self.__prioridade_tarefa_id = prioridade_tarefa_id
        self.__status_tarefa_id = status_tarefa_id
        self.__tempo_gasto_total = tempo_gasto_total
        self.__data_criacao = datetime.now()
        self.__data_conclusao = data_conclusao

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo


    @property
    def prioridade_tarefa_id(self):
        return self.__prioridade_tarefa_id

    @prioridade_tarefa_id.setter
    def prioridade_tarefa_id(self, prioridade_tarefa_id):
        self.__prioridade_tarefa_id = prioridade_tarefa_id


    @property
    def status_tarefa_id(self):
        return self.__status_tarefa_id

    @status_tarefa_id.setter
    def status_tarefa_id(self, status_tarefa_id):
        self.__status_tarefa_id = status_tarefa_id


    @property
    def tempo_gasto_total(self):
        return self.__tempo_gasto_total

    @tempo_gasto_total.setter
    def tempo_gasto_total(self, tempo_gasto_total):
        self.__tempo_gasto_total = tempo_gasto_total
    
    @property
    def data_criacao(self):
        return self.__data_criacao

    @property
    def data_conclusao(self):
        return self.__data_conclusao

    @data_conclusao.setter
    def data_conclusao(self, data_conclusao):
        self.__data_conclusao = data_conclusao




