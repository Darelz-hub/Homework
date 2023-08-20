# Создать сервис по просмотру сериала
# Для данного задания понадобится класс Сериал(название, год выхода, список актеров, режиссер, жанр, сезоны) (для сезона рекомендуется создать свой класс с атрибутами название кол-серий, список серий)
# можете выбрать любые 2 функциональности из списка ниже
# ●	реализовать общий список сериалов
# ●	реализовать возможность добавлять список любимых сериалов
# ●	реализовать возможность добавлять список любимых сезонов
# ●	реализовать возможность добавлять список любимых серий
# ●	Необходимо реализовать поиск по номеру серии, названию сезонов, названию сериалов 


class Serial:
    def __init__(self, nameserial, year,listActors,director,season, series):
        self.__nameserial = nameserial
        self.__year = year
        self.__listActors = listActors
        self.__director = director
        self.__season = season
        self.__series = series
    @property
    def show(self):
        print ( self.__nameserial, self.__year, self.__listActors,self.__director, self.__season, self.__series)