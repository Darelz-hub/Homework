# Создать сервис по просмотру сериала
# Для данного задания понадобится класс Сериал(название, год выхода, список актеров, режиссер, жанр, сезоны) (для сезона рекомендуется создать свой класс с атрибутами название кол-серий, список серий)
# можете выбрать любые 2 функциональности из списка ниже
# ●	реализовать общий список сериалов +++
# ●	реализовать возможность добавлять список любимых сериалов
# ●	реализовать возможность добавлять список любимых сезонов
# ●	реализовать возможность добавлять список любимых серий
# ●	Необходимо реализовать поиск по номеру серии, названию сезонов, названию сериалов 

from Season import Season
from Serial import Serial
import random as r
n = int(input('Сколько у вас сериалов? '))
listSerials = []
listSeason = []
listActor = ['Скала','Стетхем','Роберт Дауни младший']
for el in range(n):
    season = Season(int(input('Сколько сезонов: ')),int (input('Сколько серий в сезоне: ')))
    listSeason.append(season)

# for i in range(len(listSeason)):
#     listSeason[i].show


for el in range(n):
    serial = Serial(input('nameserial '), input('year '),listActor[r.randint(0,2)], input('director '),listSeason[el].countseason,listSeason[el].countserias)
    listSerials.append(serial)
    
#print (listSerials)
# for i in range(len(listSerials)):
#     listSerials[i].show

listfavoriteserials = []
print('------------------------------------------------------')
for el in listSerials:
    el.show
    choice = int(input('''Если хотите добавить сериал в избранное, нажмите на соответствующую цифру 
                   1. Да
                   2. Нет
                   Ваш вариант:  '''))
    if choice == 1:
        listfavoriteserials.append(el)
    else:
        continue

# for i in range(len(listfavoriteserials)):
#     listfavoriteserials[i].show
print('------------------------------------------------------')  
print('Ваши любимые сериалы:')
for i in listfavoriteserials:
        i.show   

# class Libraryserial:
#     def __init__(self,listSerials: list,listSeason: list):
#         self.__listSerials = listSerials
#         self.__listSeason = listSeason

#     # @property
#     # def getlistlibrary(self):
#     #     return self.__listSerials , self.__listSeason
    
#     @property
#     def getListSerials(self):
#         return self.__listSerials
    
#     @property
#     def getListSeason(self):
#         return self.__listSeason
    
#     def show(self):
#         for el in range(n):

#            print(self.__listSerials[el].show,'\t' ,self.__listSeason[el].show)
            
# library = Libraryserial(listSerials,listSeason)
# print('--------------------------------------------------------------') 
# print('--------------------------------------------------------------') 
# library.show()
# print('--------------------------------------------------------------') 
# print('--------------------------------------------------------------') 
# listLibrary = []
# listLibrary.append(library)
# print(listLibrary)
# print('--------------------------------------------------------------') 
# print('--------------------------------------------------------------') 
# listLibrary[0].show()
# print('--------------------------------------------------------------') 
# print('--------------------------------------------------------------') 
# listFavoriteSerials = []

# # for i,el in enumerate(listLibrary):
# #     el.show()
    
# #     choice = int(input('''Если хотите добавить сериал в избранное, нажмите на соответствующую цифру 
# #                    1. Да
# #                    2. Нет
# #                     '''))
# #     if choice == 1:
# #         listFavoriteSerials.append(el)
# #     else:
# #         continue
# # print('--------------------------------------------------------------')     
# # for el in listFavoriteSerials:
# #     el.show()

# print(len(listLibrary))
    