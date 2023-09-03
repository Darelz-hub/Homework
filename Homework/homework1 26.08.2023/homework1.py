
# ЗАДАНИЕ   
# Описать пример(в словесной или (и) в форме кода)  применения модификаторов доступа класса (public, private, protected)


class Journeyman:
    def __init__(self,name,age,profession):
        self.__learning()    
        self.name = name
        self.__age = age
        self._profession = profession  
    def __learning(self):
        print('Подмастерье обучается у мастера')
        
        
    def _create(self):
        print( self.name + ' ' + 'Создаёт')
        
    def lesson(self):
        print(self.name + ' ' + 'говорит что-то')
class Master(Journeyman):
    def __init__(self,name,age,profession,item):
        super().__init__(name,age,profession)
        self.__item = item
        
    def __str__(self):
        self._create()
        return self.__item
    
master = Master('Max','30','Кузнец','Меч')
print(master)