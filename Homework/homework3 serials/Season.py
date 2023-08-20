# Создать сервис по просмотру сериала
# Для данного задания понадобится класс Сериал(название, год выхода, список актеров, режиссер, жанр, сезоны) (для сезона рекомендуется создать свой класс с атрибутами название кол-серий, список серий)
# можете выбрать любые 2 функциональности из списка ниже
# ●	реализовать общий список сериалов
# ●	реализовать возможность добавлять список любимых сериалов
# ●	реализовать возможность добавлять список любимых сезонов
# ●	реализовать возможность добавлять список любимых серий
# ●	Необходимо реализовать поиск по номеру серии, названию сезонов, названию сериалов 


# from Serial import Serial
# from random import randint as r

class Season:
    def __init__(self, countseason: int = 1, countserias: int = 1):
        if not((type(countseason) == int) and (type(countserias) == int) ): raise 'countseason and countserias type int'
        if countserias <= 0 and countserias <= 0: raise 'countseason and countserias must >= 1'
        self.__countseason = countseason
        self.__countserias = countserias
        
    @property
    
    def countseason(self):
        return self.__countseason
    
    @property
    
    def countserias(self):
        return self.__countserias
    @property
    def show(self):
        print ( self.__countseason,self.__countserias)
        
    