class Categoria():
    def __init__(self, nome, id_categoria, titulo_projeto_id):
        self.__nome = nome
        # id do redmine
        self.__id_categoria = id_categoria
        # relacionamento com titulo_projeto
        self.__titulo_projeto_id = titulo_projeto_id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def id_categoria(self):
        return self.__id_categoria
    
    @id_categoria.setter
    def id_categoria(self, id_categoria):
        self.__id_categoria = id_categoria

    @property
    def titulo_projeto_id(self):
        return self.__titulo_projeto_id
    
    @titulo_projeto_id.setter
    def titulo_projeto_id(self, titulo_projeto_id):
        self.__titulo_projeto_id = titulo_projeto_id
