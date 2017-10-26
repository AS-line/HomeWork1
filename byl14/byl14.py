class CharaktersStalker:
	def __init__(self, relative, power, area):
		self.relative = relative
		self.power = power
		self.area = area
	def speech(self, name):
		print('Как жизьнь,', name , '?')

aloners = CharaktersStalker("Neitral", 15, "Kordon")
# aloners.speech('Сталкер?')
# print("Он на ",aloners.area)

class Enemies(CharaktersStalker):
	def __init__(self, relative, power, area, item_, guns):
		super().__init__(relative, power, area)	
		self.item_ = item_
		self.guns = guns
class Bandites(Enemies):
	def __init__(self, relative, power, area, item_, guns):
		super().__init__(relative, power, area, item_, guns)
		
	def speech(self):
		print('Заходи, не бойся - выходи не плач!')
	def damage(self):
		print("Я маслину поймал!")

aloners.speech("Барыга")

bandit = Bandites("Нейтрал", "Lox", "Cvalka", "Карманы набиты хламом", "MP5")
bandit.speech()
bandit.damage()
print(bandit.item_)
print(bandit.power)
print(bandit.guns)

class Monolites(Enemies):
	def __init__(self, relative, power, area, item_, guns):
		super().__init__(relative, power, area, item_, guns)
	def speech(self):
		print('Mooonooliiit')
	def damage(self):
		print("GGG")

monolit = Monolites("Сектант, убивающий всё подряд", "СуперСтронг", "ЧАЭС", "empty", "different powerful gunes")
monolit.speech()
monolit.damage()

# class Kinders(CharaktersStalker):
# 	def __init__(self, relative, power, area, guns)


class Kinders(CharaktersStalker):
	def __init__(self, relative, power, area, money, socially):
		super().__init__(relative, power, area)
		self.money = money
		self.socially = socially

class Scientists(Kinders):
	def __init__(self, relative, power, area, money, socially):
		super().__init__(relative, power, area, money, socially)
	def speech(self):
		print("Чем могу помочь?")

Kruglov = Scientists("Neitral", "Immortal", "Amber", "Infinitely", "Good")
Kruglov.speech()