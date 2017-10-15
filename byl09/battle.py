import random, time


def creat_player():
    player = {'hp': 100, 'урон':10}
    player['name'] = input('Введи своё имя, боец: ')
    choose = input('''Кого ты выбираешь?
1)Норд (здоровье+++ урон-)
2)Имперец (зоровье- урон+++)
3)Орк (здоровье+ урон++)\n''')
    if choose == '1':
        player['hp'] += 30
        player['урон'] -= 1
        
    elif choose == '2':
        player['hp'] -= 10
        player['урон'] += 3
        
    else:
        player['hp'] += 10
        player['урон'] += 2
    choose2 = input('''Оружие: 1)стальной меч 2)магия''')
    if choose2 == '1':
        player['урон'] += 3
    else:
        player['урон'] -= 3
    print('^'*7)
    print('Харрактеристики ', player['name'],':' , 
    	'HP=', player['hp'], 'Урон=', player['урон'])
    print('_'*7)
    return player




def show_health(player):
    print('Количество хп', player['name'],': ' , player['hp'])

def attack(attacker, victim):
    damage = random.randint(attacker["урон"] - 4 , attacker["урон"])
    victim['hp'] -= damage
    if damage > attacker["урон"] - 1:
        print(attacker['name'], 'нанёс сокрушительный удар', damage)
    else:
        print(attacker['name'], 'нанёс', damage,
     ' едениц урона')
    





player1 = creat_player()
player2 = creat_player()

while True:
    if player1['hp'] <= 0:
        print(player2['name'], ' выйграл!')
        break
    elif player2['hp'] <= 0:
        print(player1['name'], ' выйграл!')
        break
    attack(player1, player2)
    attack(player2, player1)

    show_health(player1)
    show_health(player2)

    input()


