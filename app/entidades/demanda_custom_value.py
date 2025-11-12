class DemandaCustomValue():
    def __init__(self, texto, custom_fields_id, demanda_id):
        self.__texto = texto
        self.__custom_fields_id = custom_fields_id
        self.__demanda_id = demanda_id

    @property
    def texto(self):
        return self.__texto
    
    @texto.setter
    def texto(self, texto):
        self.__texto = texto

    @property
    def custom_fields_id(self):
        return self.__custom_fields_id
    
    @custom_fields_id.setter
    def custom_fields_id(self, custom_fields_id):
        self.__custom_fields_id = custom_fields_id
    
    @property
    def demanda_id(self):
        return self.__demanda_id
    
    @demanda_id.setter
    def demanda_id(self, demanda_id):
        self.__demanda_id = demanda_id