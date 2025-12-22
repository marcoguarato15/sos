from datetime import datetime

class Atividade():
    def __init__(self, titulo, tarefa_id, tempo_estimado, categoria_atividade_id, status_tarefa_id, usuarios, data_conclusao=None):
        self.__titulo = titulo
        self.__tarefa_id = tarefa_id
        self.__tempo_estimado = tempo_estimado
        self.__categoria_atividade_id = categoria_atividade_id
        self.__data_criacao = datetime.now()
        self.__data_conclusao = data_conclusao
        self.__status_tarefa_id = status_tarefa_id
        self.__usuarios = usuarios

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def tarefa_id(self):
        return self.__tarefa_id
    
    @tarefa_id.setter
    def tarefa_id(self, tarefa_id):
        self.__tarefa_id = tarefa_id

    @property
    def tempo_estimado(self):
        return self.__tempo_estimado
    
    @tempo_estimado.setter
    def tempo_estimado(self, tempo_estimado):
        self.__tempo_estimado = tempo_estimado

    @property
    def categoria_atividade_id(self):
        return self.__categoria_atividade_id
    
    @categoria_atividade_id.setter
    def categoria_atividade_id(self, categoria_atividade_id):
        self.__categoria_atividade_id = categoria_atividade_id

    @property
    def data_criacao(self):
        return self.__data_criacao

    @property
    def data_conclusao(self):
        return self.__data_conclusao
    
    @data_conclusao.setter
    def data_conclusao(self, data_conclusao):
        self.__data_conclusao = data_conclusao

    @property
    def status_tarefa_id(self):
        return self.__status_tarefa_id
    
    @status_tarefa_id.setter
    def status_tarefa_id(self, status_tarefa_id):
        self.__status_tarefa_id = status_tarefa_id

    @property
    def usuarios(self):
        return self.__usuarios
    
    @usuarios.setter
    def usuarios(self, usuarios):
        self.__usuarios = usuarios