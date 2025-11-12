class TutiloProjeto():
    def __init__(self, nome, id_titulo_projeto):
        self.__nome = nome
        self.__id_titulo_projeto = id_titulo_projeto

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def id_titulo_projeto(self):
        return self.__id_titulo_projeto
    
    @id_titulo_projeto.setter
    def id_titulo_projeto(self, id_titulo_projeto):
        self.id_titulo_projeto = id_titulo_projeto

    """
    id do project name (tipo de solicitação)
    6 - Projetos de Redes Digitais
    8 -  Serviços de rede
    10 - Infraestrutura de rede
    """