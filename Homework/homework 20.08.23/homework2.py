# Описать пример(в словесной или (и) в форме кода)  применения Абстрактного класса
class Bird:
    
    
    def say(self):
        print('Птица ничего не говорит')
        
class Сhicken(Bird):
    def __init__(self,name):
        self.__name = name
        
    def say(self):
        print('Курица кудахчет')
        

class Duck(Bird):
    def __init__(self,name):
        self.__name = name
        
        
    def say(self):
        print('Утка говорит кря кря')
        
class Ostrich(Bird):
    def __init__(self,name):
        self.__name = name
        
chicken = Сhicken('Проша')
chicken.say()

duck = Duck('Дак')
duck.say()

osrtich = Ostrich('Василий')
osrtich.say()



# Описать пример (в словесной или (и) в форме кода) Множественного наследования

class Blade:
    
    def atack_blade(self):
        print('Вы можете атаковать клинком, но пораните себя')
        
class Handle:
    def doing_handle(self):
        print("вы можете держать рукоять, но не можете атаковать")
        
class Sword(Blade,Handle):
    def doing(self):
        print('Вы объединили клинок и рукоять в меч ,теперь вы можете атаковать и держать меч, не боясь пораниться')
        
