class CategoriaAtividade():
    def __init__(self, nome, ordem_execucao):
        self.__nome = nome
        self.__ordem_execucao = ordem_execucao

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ordem_execucao(self):
        return self.__ordem_execucao
    
    @ordem_execucao.setter
    def ordem_execucao(self, ordem_execucao):
        self.__ordem_execucao = ordem_execucao