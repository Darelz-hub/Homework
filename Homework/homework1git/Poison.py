class Poison():
    def __init__(self, name: str, price: int, item: dict):
        self.__name = name
        self.__price = price
        self.__item = item # рецепт
    @property
    
    def name(self):
        return self.__name
    
    @property
    
    def price(self):
        return self.__price
    
    @property
    def item(self):
        return self.__item
    
    
    def check_components(self,people_choice: int,mainitem:dict):
        mainitem = mainitem
        if people_choice == 1:
            if  mainitem['plantain'] >= self.item['plantain']:
                print('Вы можете создать целебный отвар')
                return True
            else:
                print('Вы не можете создать зелье ')
                return False
        elif people_choice == 2:
            if mainitem['plantain'] >= self.item['plantain'] and mainitem['parsley'] >= self.item['parsley']:
                print('Вы можете создать Приятель')
                return True
            else:
                print('Вы не можете создать зелье ')
                return False
        elif people_choice == 3:
            if mainitem['parsley'] >= self.item['parsley'] and mainitem['plantain'] >= self.item['plantain']  and mainitem['cheremukh'] >= self.item['cheremukh']:
                print('Вы можете создать зелье Прилив сил')
                return True
            else:
                print('Вы не можете создать зелье ')
                return False
            