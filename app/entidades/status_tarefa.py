class StatusTarefa():
    def __init__(self, num_status, nome):
        self.__num_status = num_status
        self.__nome = nome

    @property
    def num_status(self):
        return self.__num_status

    @num_status.setter
    def num_status(self, num_status):
        self.__num_status = num_status

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

        