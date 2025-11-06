from datetime import datetime

class Horario_trabalho():
    def __init__(self, horario_inicio, horario_fim, tipo_turno, criador_id=None, ultima_atualizacao=None):
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipo_turno = tipo_turno
        self.__criador_id = criador_id
        self.__data_criacao = datetime.now()
        self.__ultima_atualizacao = ultima_atualizacao

    @property
    def horario_inicio(self):
        return self.__horario_inicio
    
    @horario_inicio.setter
    def horario_inicio(self, horario_inicio):
        self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim
    
    @horario_fim.setter
    def horario_fim(self, horario_fim):
        self.__horario_fim = horario_fim

    @property
    def tipo_turno(self):
        return self.__tipo_turno
    
    @tipo_turno.setter
    def tipo_turno(self, tipo_turno):
        self.__tipo_turno = tipo_turno

    @property
    def criador_id(self):
        return self.__criador_id

    @property
    def data_criacao(self):
        return self.__data_criacao
    
    @property
    def ultima_atualizacao(self):
        return self.__ultima_atualizacao
    
    @ultima_atualizacao.setter
    def ultima_atualizacao(self, ultima_atualizacao):
        self.__ultima_atualizacao = ultima_atualizacao