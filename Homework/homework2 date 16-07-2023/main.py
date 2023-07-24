# Создать Корзина товаров -> список товаров пользователя
# Для данного задания понадобится класс товар (название, тип(одежда, обувь, украшение), стоимость)
# + реализовать общий список всех товаров
#+ список добавленных товаров в корзину
#
# необходимо реализовать возможность подсчета стоимости товаров в корзине -> геттер для cost
from Product import Product
from random import randint as r# r(start,end) === random.randint(start,end)

#список всех товаров в магазине
list_products = [Product('short', 'одежда', 250), Product('boots', 'обувь', 2000), Product('jerry', 'украшение', 10000)]

i = 1
shop_cart = [ ]
for product in list_products:
    print(str(i)+". ", end='')
    product.show()
    i+=1
   
#цикл для добавления товаров пользователем 
sum = 0
while True:
    #номер товара опеделяет пользователь
    
    user_choice = input('would you like the product of number ... ')# дописать условия добавления и т.д. выход из системы
    if user_choice == '0':
        break
    elif user_choice == '1': 
        # people = list_products[int(user_choice)-1]
        # sum += people.cost
        sum += list_products[int(user_choice)-1].cost #list_products[0] - Product('short', 'одежда', 250) -> Product('short', 'одежда', 250).cost 
        #print(sum)
        shop_cart.append(list_products[int(user_choice)-1]) #добавит блок проверки перед добавлением в корзину попапку
    elif user_choice == '2':
        sum += list_products[int(user_choice)-1].cost
        shop_cart.append(list_products[int(user_choice)-1])
        #print(sum)
        #print(type(sum))
    elif user_choice == '3':
        sum += list_products[int(user_choice)-1].cost
        shop_cart.append(list_products[int(user_choice)-1])
        #print(sum)
print(sum) # спросить про место print, почему он не срабатывает в данном мессте, А СРАБАТЫВАЕТ, только после конечного цикла


# список добавленных товаров в корзину
i = 1
print('\n ***************shop_cart***************')
for product in shop_cart:
    print(str(i)+". ", end='')
    product.show()
    i+=1
#print(sum) # здесь он работает 















# через класс магазин
# Создать класс Корзина товаров ->
# Для данного задания понадобится класс товар (название, тип(одежда, обувь, украшение), стоимость)
# реализовать общий список всех товаров
# список добавленных товаров в корзину
# необходимо реализовать возможность подсчета товаров






