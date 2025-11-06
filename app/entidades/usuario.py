from datetime import datetime

class Usuario():
    def __init__(self, nome, email, senha, cargo, setor_id, ativo, papel, disponivel, contato, criador_id, horario_trabalho_id=None, ultima_atualizacao=None, ultimo_login=None, deletado_em=None):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__cargo = cargo
        self.__setor_id = setor_id
        self.__ativo = ativo
        self.__papel = papel
        self.__disponivel = disponivel
        self.__contato = contato
        self.__criador_id = criador_id
        self.__data_criacao = datetime.now()
        self.__ultima_atualizacao = ultima_atualizacao
        self.__ultimo_login = ultimo_login
        self.__deletado_em = deletado_em
        self.__horario_trabalho_id = horario_trabalho_id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def setor_id(self):
        return self.__setor_id
    
    @setor_id.setter
    def setor_id(self, setor_id):
        self.__setor_id = setor_id

    @property
    def ativo(self):
        return self.__ativo
    
    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo

    @property
    def papel(self):
        return self.__papel
    
    @papel.setter
    def papel(self, papel):
        self.__papel = papel

    @property
    def disponivel(self):
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel):
        self.__disponivel = disponivel

    @property
    def contato(self):
        return self.__contato
    
    @contato.setter
    def contato(self, contato):
        self.__contato = contato

    @property
    def criador_id(self):
        return self.__criador_id
    
    @criador_id.setter
    def criador_id(self, criador_id):
        self.__criador_id = criador_id

    @property
    def data_criacao(self):
        return self.__data_criacao

    @property
    def ultima_atualizacao(self):
        return self.__ultima_atualizacao
    
    @ultima_atualizacao.setter
    def ultima_atualizacao(self, ultima_atualizacao):
        self.__ultima_atualizacao = ultima_atualizacao

    @property
    def ultimo_login(self):
        return self.__ultimo_login
    
    @ultimo_login.setter
    def ultimo_login(self, ultimo_login):
        self.__ultimo_login = ultimo_login

    @property
    def deletado_em(self):
        return self.__deletado_em
    
    @deletado_em.setter
    def deletado_em(self, deletado_em):
        self.__deletado_em = deletado_em

    @property
    def horario_trabalho_id(self):
        return self.__horario_trabalho_id
    
    @horario_trabalho_id.setter
    def horario_trabalho_id(self, horario_trabalho_id):
        self.__horario_trabalho_id = horario_trabalho_id

