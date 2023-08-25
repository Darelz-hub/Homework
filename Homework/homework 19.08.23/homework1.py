# 1.
# реализуйте класс Student и класс Aspirant, аспирант отличается от студента наличием некой научной работы.
# Класс Student содержит переменные: String firstName, lastName, group. А также, double averageMark, содержащую среднюю оценку.
# Создать метод getScholarship() для класса Student, который возвращает сумму стипендии. Если средняя оценка студента равна 5, то сумма 2000, иначе 1900. Переопределить этот метод в классе Aspirant.  Если средняя оценка аспиранта равна 5, то сумма 2500, иначе 2200.
# Создать массив типа Student, содержащий объекты класса Student и Aspirant. Вызвать метод getScholarship() для каждого элемента массива.
# ●	НЕОБЯЗАТЕЛЬНО ->Усложнение сделать через наследование 


class Student:
    
    def __init__(self, firstName:str,lastName:str,group:str, averageMark: float,):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__group = group
        self.__averageMark = averageMark

    @property
    def averageMark(self):
        return self.__averageMark 
    
    @property
    
    def getScholarship(self):
        if self.averageMark == 5.0:
            print('Ваша стипендия: 2000 рублей')
        else:
            print('Ваша стипендия: 1900 рублей')
#----------------------------------Check--------------------   
    # def __str__(self):
    #     return 'Имя: ' + self.__firstName + ' Фамилия ' + self.__lastName + ' Группа: ' + self.__group + ' Средняя оценка: ' + str(self.__averageMark)
# student = Student('www','www','www', 5) # Check
# student.getScholarship
# print(student)
# ---------------------------------------------------------------


class Aspirant(Student):
    def __init__(self,firstName:str,lastName:str,group:str, averageMark: float, scientificWork:str):
        super().__init__(firstName,lastName,group, averageMark)
        self.__scientificWork = scientificWork
    
    @property
    
    def getScholarship(self):
        if self.averageMark == 5.0:
            print('Ваша стипендия: 2500 рублей')
        else:
            print('Ваша стипендия: 2200 рублей')
            
            
listPeople = [Student("Max","Ivanov",'21',5), Aspirant('Petr','Petrov','40',4,'Война и мир'),Student('Vlad','Vladov','32',4.5),Aspirant('Igor',"Ivanov",'45',5,'Дружба')]

for el in listPeople:
    el.getScholarship




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 2.
# Создать класс Person, который содержит: 

# переменные fullName, age - должны быть закрыты;
# методы move() и talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит". 
# создайте геттеры и сеттеры для закрытых полей класса
# Создайте два объекта этого класса. 
# Вызовите методы move() и talk().


class Person:
    def __init__(self,fullName:str, age:int):
        if not(type(age)) == int: raise 'age must be of type int'
        if age <= 0: raise 'age must be >= 0'
        self.__fullName = fullName
        self.__age = age
        
    def move(self):
        return self.__fullName + ' ' + 'Делает зарядку'
    
    def talk(self):
        return self.__fullName + ' Говорить, о хорошей погоде '
    
    @property
    def fullName(self):
        return self.__fullName
    
    @fullName.setter
    def fullName(self, fullName):
        self.__fullName = fullName
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age = age
    
    def __str__(self):
        return self.fullName + ' ' + str(self.age)
person = Person('Ivan', 20)

print(person)

person.age = 24
person.fullName = 'Max'
print(person)
print(person.talk())
print(person.move())