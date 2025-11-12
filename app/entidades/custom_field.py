class CustomField():
    def __init__(self, nome, id_custom_field):
        self.__nome = nome
        self.__id_custom_field = id_custom_field

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def id_custom_field(self):
        return self.__id_custom_field
    
    @id_custom_field.setter
    def id_custom_field(self, id_custom_field):
        self.__id_custom_field = id_custom_field