class DemandaCustomValue():
    def __init__(self, valor, custom_field_id, demanda_id):
        self.__valor = valor
        self.__custom_field_id = custom_field_id
        self.__demanda_id = demanda_id

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def custom_field_id(self):
        return self.__custom_field_id
    
    @custom_field_id.setter
    def custom_field_id(self, custom_field_id):
        self.__custom_field_id = custom_field_id
    
    @property
    def demanda_id(self):
        return self.__demanda_id
    
    @demanda_id.setter
    def demanda_id(self, demanda_id):
        self.__demanda_id = demanda_id