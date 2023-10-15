class Users():
    def __init__(self, name: str, cname: str, postal_code: str):
        self.__name = name
        self.__cname = cname
        self.__postal_code = postal_code
        
    @property
    def name(self):
        return self.__name
    
    @property
    def cname(self):
        return self.__cname
    
    @property
    def postal_code(self):
        return self.__postal_code