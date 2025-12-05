class StatusTarefa():
    def __init__(self, em_andamento, nome):
        self.__em_andamento = em_andamento
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def em_andamento(self):
        return self.__em_andamento

    @em_andamento.setter
    def em_andamento(self, em_andamento):
        self.__em_andamento = em_andamento

        