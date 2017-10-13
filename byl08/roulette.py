import random, math

player1 = {'фишки': 500}

player1["name"] = input('Игрок 1: ')

game = int(input("""На что ставите:
1)цвет
2)цифру\n"""))
if game == 1:
    while True:
        player1['ставка'] = math.fabs(int(input(player1['name'] + ", Ваша ставкa: ")))
        player1['выбор'] = int(input('''Какой цвет вы выбираете?
1)черный
2)красный\n'''))
        player1['выбор'] = random.randint()
        kazino 
        if kazino == player1['выбор']:
            print('Поздравляем, вы правильно угадали цвет')
            player1['фишки'] += player1['ставка'] * 2
            print(player1["name"], ', Ваш счет: ', player1['фишки'])
        elif kazino != player1['выбор']:
            print('Сожалеем, но вы не угадали')
            player1['фишки'] -= player1['ставка']
            print(player1["name"], ', Ваш счет: ', player1['фишки'])
        if player1['фишки'] <= 0:
            print(player1['name'], ' пройграл')
            break
elif game == 2:       
    wh = int(input('На какую цифру ставите?\
1)Ввести\
2)Все'))
    if wh == 1:
        while True:       
            player1['выбор'] = math.fabs(int(input("Вводите цифру, выбранную Вами: ")))
            player1['ставка'] = math.fabs(int(input(player1['name'] + ", Ваша ставка: ")))
            kazino = random.randint(1, 37) 
            if kazino == player1['выбор']:
                print('Поздравляем, вы правильно угадали цифру')
                print('''************
Правильный ответ: ''', kazino)
                player1['фишки'] += player1['ставка'] * 36
                print(player1["name"], ', Ваш счет: ', player1['фишки'])
            elif kazino != player1['выбор']:               
                print('Сожалеем, но вы не угадали')
                print('''************
Правильный ответ: ''', kazino)
                player1['фишки'] -= player1['ставка']
                print(player1["name"], ', Ваш счет: ', player1['фишки'])
            elif player1["фишки"] <= 0:
                print(player1['name'], ' пройграл')
                break
            print('*' * 70)
    elif wh == 2:
        while True:
            player1['ставка'] = math.fabs(int(input(player1['name'] + ", Ваша ставка: ")))
            kazino = random.randint(0, 37)
            if kazino == 0:
                print('правильный ответ: ', kazino)
                print('Сожалеем, но вы не угадали')
                player1['фишки'] -= player1['ставка']
                print(player1["name"], ', Ваш счет: ', player1['фишки'])
            elif kazino != 0:
                print('Поздравляем, вы правильно угадали цвет')
                player1['фишки'] += player1['ставка'] * 36
                print(player1["name"], ', Ваш счет: ', player1['фишки'])
            elif player1["фишки"] <= 0:
                print(player1['name'], ' пройграл')
                break
            print('*' * 70)