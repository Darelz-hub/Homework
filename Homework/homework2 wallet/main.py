
# ЗАДАНИЕ 1 (Обязательно) 
# на выбор два класса
	
# 1.	Создать класс кошелек с атрибутами в виде:
# a.	баланс 
# b.	магический метод на выбор:
# i.	увелечение баланса на n
# ii.	Сравнение двух кошельков
# iii.	проверку баланса на ноль
# iv.	предложить ваш метод

class Wallet:
    # a.	баланс 
    def __init__(self,balance: int = 0):
        # iii.	проверку баланса на ноль
        if not(balance > 0): raise 'balance > 0'
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    @property
    def show(self):
        print(self.__balance)
        
    # i.	увелечение баланса на n
    def __add__(self,replenishment):
        self.__balance += replenishment
        return self
    
    def __add__(self,replenishment):
        return self.balance + replenishment
    
    # iv.	предложить ваш метод
    def __sub__(self,subtraction):
        if not(self.__balance > 0 and self.__balance >= subtraction): raise 'self.__balance > 0 and self.__balance > = subtraction'
        self.__balance -= subtraction
        return self
    
    # # ii.	Сравнение двух кошельков
    # def __eq__(self,wallet2): 
    #     if self.balance > wallet2.balance:
    #         print('wallet1 > wallet2')
    #     elif self.balance< wallet2.balance:
    #         print('wallet1 < wallet2 ') 
    #     else:
    #         print('wallet1 = wallet2')
wallet = Wallet(100000)
wallet2 = Wallet(5000)
b = wallet + 900
print(b)
#print(type(b))
c = wallet + 1000
c = wallet - 200
c.show
#print(c)
# d = (wallet == wallet2)

