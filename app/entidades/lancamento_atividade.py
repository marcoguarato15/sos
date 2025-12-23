from datetime import datetime

class LancamentoAtividade():
    def __init__(self, usuario_id, atividade_id, descricao, tempo_gasto):
        self.__usuario_id = usuario_id
        self.__atividade_id = atividade_id
        self.__descricao = descricao
        self.__tempo_gasto = tempo_gasto
        self.__data_criacao = datetime.now()

    @property
    def usuario_id(self):
        return self.__usuario_id
    
    @usuario_id.setter
    def usuario_id(self, usuario_id):
        self.__usuario_id = usuario_id

    @property
    def atividade_id(self):
        return self.__atividade_id
    
    @atividade_id.setter
    def atividade_id(self, atividade_id):
        self.__atividade_id = atividade_id

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def tempo_gasto(self):
        return self.__tempo_gasto
    
    @tempo_gasto.setter
    def tempo_gasto(self, tempo_gasto):
        self.__tempo_gasto = tempo_gasto

    @property
    def data_criacao(self):
        return self.__data_criacao