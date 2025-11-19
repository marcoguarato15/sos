class Demanda():
    # situacao_id = tracker(situação)
    # categoria_id = category_id
    def __init__(self, id_demanda, titulo_projeto_id, titulo,  tipo_id, status_id, prioridade_id, author_id, categoria_id, data_criacao, porcentagem_feita, ativo, descricao=None, atribuido_para_id=None, data_inicio=None, data_atualizacao=None, data_finalizacao=None):
        # campos definidos
        self.__id_demanda = id_demanda
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_inicio = data_inicio
        self.__data_criacao = data_criacao
        self.__data_atualizacao = data_atualizacao
        self.__data_finalizacao = data_finalizacao
        self.__porcentagem_feita = porcentagem_feita
        self.__ativo = ativo
        # relacionamento com usuario
        self.__author_id = author_id
        self.__atribuido_para_id = atribuido_para_id
        # relacionamentos por necessidade de id_demanda
        self.__tipo_id = tipo_id
        self.__status_id = status_id
        self.__titulo_projeto_id = titulo_projeto_id
        self.__prioridade_id = prioridade_id
        self.__categoria_id = categoria_id

    @property
    def id_demanda(self):
        return self.__id_demanda
    
    @id_demanda.setter
    def id_demanda(self, id_demanda):
        self.__id_demanda = id_demanda

    @property
    def titulo_projeto_id(self):
        return self.__titulo_projeto_id
    
    @titulo_projeto_id.setter
    def titulo_projeto_id(self, titulo_projeto_id):
        self.__titulo_projeto_id = titulo_projeto_id

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def tipo_id(self):
        return self.__tipo_id
    
    @tipo_id.setter
    def tipo_id(self, tipo_id):
        self.__tipo_id = tipo_id

    @property
    def status_id(self):
        return self.__status_id
    
    @status_id.setter
    def status_id(self, status_id):
        self.__status_id = status_id

    @property
    def prioridade_id(self):
        return self.__prioridade_id
    
    @prioridade_id.setter
    def prioridade_id(self, prioridade_id):
        self.__prioridade_id = prioridade_id

    @property
    def author_id(self):
        return self.__author_id
    
    @author_id.setter
    def author_id(self, author_id):
        self.__author_id = author_id

    @property
    def categoria_id(self):
        return self.__categoria_id
    
    @categoria_id.setter
    def categoria_id(self, categoria_id):
        self.__categoria_id = categoria_id

    @property
    def atribuido_para_id(self):
        return self.__atribuido_para_id
    
    @atribuido_para_id.setter
    def atribuido_para_id(self, atribuido_para_id):
        self.__atribuido_para_id = atribuido_para_id

    @property
    def data_inicio(self):
        return self.__data_inicio
    
    @data_inicio.setter
    def data_inicio(self, data_inicio):
        self.__data_inicio = data_inicio

    @property
    def data_criacao(self):
        return self.__data_criacao
    
    @data_criacao.setter
    def data_criacao(self, data_criacao):
        self.__data_criacao = data_criacao

    @property
    def data_atualizacao(self):
        return self.__data_atualizacao
    
    @data_atualizacao.setter
    def data_atualizacao(self, data_atualizacao):
        self.__data_atualizacao = data_atualizacao

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao
    
    @data_finalizacao.setter
    def data_finalizacao(self, data_finalizacao):
        self.__data_finalizacao = data_finalizacao

    @property
    def ativo(self):
        return self.__ativo
    
    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo

    @property
    def porcentagem_feita(self):
        return self.__porcentagem_feita
    
    @porcentagem_feita.setter
    def porcentagem_feita(self, porcentagem_feita):
        self.__porcentagem_feita = porcentagem_feita