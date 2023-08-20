# ЗАДАНИЕ 1 (Обязательно) 
# представим себе игру стратегию. Напишите в комментариях логику, которую вы видете по взаимодействию с этими башнями
# Создать класс башня (есть броня и здоровье, а также регуляторы увеличения и уменьшения здоровья и брони). Создать класс стрелковая башня (умеет стрелять и все то, что и родитель)

class Tower:
    def __init__(self,hp: int  = 100, cp: int = 100):
        self.__hp = hp
        self.__cp = cp
        self.__doing = 'Стоит'
    
    
    def show(self):
        print ( self.__hp, self.__cp, self.__doing)
    
    @property
    
    def hp(self):
        return self.__hp
    
    @property
    
    def cp(self):
        return self.__cp
    @property
    
    def doing(self):
        return self.__doing
    
    def __sub__(self, n):
        cp = n
        hp = cp/2
        self.__hp -= hp 
        self.__cp -= cp
        #return self
        
class ShootTower(Tower):
    
    def __init__(self, hp: int = 70, cp: int = 50):
        super().__init__(hp,cp)
        self.__action = 'Стрелять'
    
    def show(self):
        print( self.hp,self.cp,self.doing, self.__action )
        
tower = Tower()
tower.show()
n = int(input('Введите урон'))
tower - n
tower.show()
tower1 = ShootTower()
n = int(input('Введите урон'))
tower1 - n
tower1.show()


