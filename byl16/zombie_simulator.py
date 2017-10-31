import random, time, os

frases_zombie_end = ["УУУУуууу", "Мляяяяяя", "ЗЗЗЗЗЗЗ", "ПЫХпых", ' Xы-Хы-Хы ']
frases_end = [" умудрился замочить ", " убил ", " смог умертвить ", " закопал ", " похоронил "]

class Human:
	def __init__(self, health, damage):
		self.health = health
		self.damage = damage

	def attack(self, target):
		time.sleep(1.5)
		урон = random.randint(self.damage - 2, self.damage + 2)
		target.health -= урон
		print(' ' ,self.name, 'ударил противника с неимоверной силой и унёс ', урон, ' HP')


class Player(Human):
	def __init__(self, health, damage, count_kit, name):
		super().__init__(health,damage)
		self.count_kit = count_kit
		self.name = name

	def heal(self):
		if self.count_kit > 0:
			self.count_kit -= 1
			self.health += 15
			print( "Вы воспользовались аптечкой. Ваше здоровье:", self.health)
			time.sleep(1)
		else:
			print(" Cорян, аптечек больше нет, терпи!")
			time.sleep(1)

class Zombie(Human):
	def __init__(self, health, damage, name):
		super().__init__(health, damage)
		self.name = name
	def death(self, killer):
		print(' ' ,random.choice(frases_zombie_end), " - умер один зомби, но из его живота выскочил другой)\
			к количеству убитыx зомби +1")
		chance = random.randint(1,4)
		if chance in (2,3):
			print(" Из 'мёртвого' мертвеца выпал набор для шитья, которым можно себя подлотать(аптечки+1)")
			killer.count_kit += 1


def anim_search():  #Анимация троеточия, подсмотренная у Лукмана:)
	time.sleep(0.5)
	os.system('cls')
	print("Поиск")
	time.sleep(0.5)
	os.system('cls')
	print("Поиск.")
	time.sleep(0.5)
	os.system('cls')
	print("Поиск..")
	time.sleep(0.5)
	os.system('cls')
	print("Поиск...")
	time.sleep(0.5)
	os.system('cls')
	print("Поиск")
	time.sleep(0.5)
	os.system('cls')
	print("Поиск.")
	time.sleep(0.5)
	os.system('cls')
	print("Поиск..")
	time.sleep(0.5)
	os.system('cls')
	print("Поиск...")
	time.sleep(0.5)
	os.system('cls')

def game():
	коэффициент = 2
	count_kill = 0
	man = Player(100, 10, 3, None)
	zombie = Zombie(30, 15, None)
	man.name = input(' Введите своё имя:')
	zombie.name = input(' Как обзывём зомби?:')
	выбор = int(input(' '+ man.name + ''', чем махаться будешь?
 1)ПМ(+4 к урону, +10 к крутости)
 2)Обрез(+6 к урону, + 3 к крутости)
 3)Что-нибудь из хлама(+? к урону(супер рандом), -1 к крутости)
 4)Руки(+0 к урону, +20 к крутости, -10 жира)\n>>>'''))
	os.system('cls')
	if выбор == 1:
		man.damage += 4
		коэффициент += 10
		print('Битва началась!')
		time.sleep(2)
	elif выбор == 2:
		man.damage += 6
		коэффициент += 3
		print('FIGHT!')
		time.sleep(2)
	elif выбор == 3:
		anim_search()
		нечто = random.randint(-1, 10)
		man.damage += нечто
		коэффициент -= 1
		if нечто in (-1, 0, 1):
			print('>>>>Ты откопал убитую гаусс-пушку, которая клинит при каждом выстреле(урон ', нечто,')')
		elif нечто in (2, 3, 4, 5):
			print('>>>>Ты нашел СВД палеозойской эпохи(урон ', нечто,')')
		elif нечто in (6, 7):
			print('>>>>Ты нашел АК-73 среднего качества(урон ', нечто,')')
		elif нечто in (8, 9, 10):
			print('>>>>Ты добыл карманный рельсотрон(урон ', нечто,')')
		print('Да начнётся ИГРА!')
		time.sleep(2)
	else:
		print("=>Твоя воля - твои правила!")
		print('Да начнётся БИТВА!')
		коэффициент += 20
		
	while True:
		if man.health <= 0:
			print(man.name, random.choice(frases_end), count_kill,
				' зомбяков')
			print(' Ты заработал ',count_kill*коэффициент, "очков")
			break
		man.attack(zombie)
		time.sleep(1.5)
		zombie.attack(man)
		input()
		os.system('cls')
		if zombie.health <= 0: #Умирает зомби
			zombie.death(man)
			zom2_name = input(" Как назовёшь дочернего зомби?\n")
			zombie = Zombie(25, 12, zom2_name)
			count_kill += 1
		print(" Оптечек: ", man.count_kit)
		print(" HP: ", man.health,
			" Скушать аптечку?(+15HP)")
		i = int(input(" 1)Да" + " 2)Нет\n>>>"))
		if i == 1:
			man.heal()
		time.sleep(0.5)
		os.system('cls')
os.system('cls')
time.sleep(2)
print("▒"*70)
print(" Приветствуем в первом текстовом симуляторе батла с зомби(v5.1)")
print(""" Всё на русском языке!
 захватывающий гемплей!
 качественная текстовая графика!
 Правила предельно просты: вам требуется придумать имя зомби и ввести своё.
 Затем просто БИТЬСЯ!""")
print("▒"*70)
input('Для подолжения нажмите ENTER')
time.sleep(1)

game() #Запускается весь игровой процесс