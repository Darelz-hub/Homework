from Poison import *
mainitem = {'plantain': 4, 'parsley': 3, 'cheremukh': 4, 'Целебный отвар': 0, 'Приятель': 0, 'Прилив сил': 0, 'balance': 0}

listPoison = [Poison('Целебный отвар',100, {'plantain': 2}), Poison('Приятель',200, {'plantain': 2, 'parsley': 1}),Poison('Прилив сил',300, {'plantain': 2, 'parsley': 1,'cheremukh': 3} )]


while True:
    print('''
          Что вы хотите сделать?
          1. Создать зелье
          2. Продать зелье
          3. Показать инвентарь
          4. Выход
          ''')
    people_choice = int(input('Ваш выбор: '))
    if people_choice == 1:
    
        while True:
            print('''
              Какое зелье вы хотите создать?
              1.Целебный отвар
              2.Приятель
              3.Прилив сил
              4.Выйти
              ''')
            people_choice = int(input('Ваш выбор: '))
            if people_choice == 1:
                if listPoison[0].check_components(people_choice,mainitem):
                    mainitem['Целебный отвар'] += 1
                    mainitem['plantain'] -= 2
            elif people_choice == 2:
                if listPoison[1].check_components(people_choice, mainitem):
                    mainitem['Приятель'] += 1
                    mainitem['plantain'] -= 2
                    mainitem['parsley'] -= 1
            elif people_choice == 3:
                if listPoison[2].check_components(people_choice, mainitem):
                    mainitem['Прилив сил'] += 1
                    mainitem['plantain'] -= 2
                    mainitem['parsley'] -= 1
                    mainitem['cheremukh'] -= 3
            elif people_choice == 4:
                break
    
    elif people_choice == 2:
        while True:
            print('''Что вы хотите сделать:
                1. Продать зелье Целебный отвар
                2. Продать зелье Приятель
                3. Продать зелье Прилив сил
                4. Посмотреть баланс
                5. Выход
                ''')
            people_choice = int(input('Ваш выбор: '))
            if people_choice == 1:
                if mainitem['Целебный отвар'] > 0:
                    mainitem['Целебный отвар'] -= 1
                    mainitem['balance'] += listPoison[0].price
                else:
                    print('У вас нет этого зелья')
            elif people_choice == 2:
                if mainitem['Приятель'] > 0:
                    mainitem['Приятель'] -= 1
                    mainitem['balance'] += listPoison[1].price
                else:
                    print('У вас нет этого зелья')
            elif people_choice == 3:
                if mainitem['Прилив сил'] > 0:
                    mainitem['Прилив сил'] -= 1
                    mainitem['balance'] += listPoison[2].price
                else:
                    print('У вас нет этого зелья')
            elif people_choice == 4:
                print(mainitem['balance'])
            elif people_choice == 5:
                break
    elif people_choice == 3:
        print(mainitem)
    elif people_choice == 4:
        break