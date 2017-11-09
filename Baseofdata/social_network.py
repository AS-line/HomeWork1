import os, time
os.system('cls')
class Users():
	def __init__(self, login, password, name, surname, age, country, language, cash):
		self.login = login
		self.password = password
		self.name = name
		self.surname = surname
		self.age = age
		self.country = country
		self.language = language
		self.cash = cash
	def regist(self):
		f = open(self.login,"w")
		data = [self.password, self.name, self.surname, self.age, self.country, self.language, self.cash]
		f.write(str(data))
		print('===============Успешная регистрация===============')
		print('Поздравяем! Вы получаете 5000 бонусных рублей!')
		f.close()
		input('Войти ENTER')
		self.enter()
	def enter(self):
		f = open(self.login,"r")
		true_password = f.read()
		true_password = true_password.split("'")
		if self.password == true_password[1]:
			os.system('cls')
			print('===============Успешная авторизация===============')
			self.actions()
			return self.login
		elif self.password != true_password:
			print("Неверный пароль")
			work_again()
		f.close()
	def actions(self):
		act = input('''Действия с аккаунтом:
1)Показать данные профиля
2)Магазин
3)Изменить данные
>>>''')
		if act == '1':
			self.show_profile()
		elif act == '3':
			os.system('cls')
			print("===============Изменение профиля===============")
			print('Текущие данные:')
			self.show_profile()
			self.edit_profile()
		elif act == '2':
			buying(self.login)
				
	def show_profile(self):
		f = open(self.login,"r")
		acc_list = f.read()
		acc_list = acc_list.split("'")
		acc_name = acc_list[3]
		acc_surname = acc_list[5]
		acc_age = acc_list[7]
		acc_country = acc_list[9]
		acc_language = acc_list[11]
		acc_cash = acc_list[13]
		print('Логин:', self.login)
		print('Имя:', acc_name)
		print('Фамилия:', acc_surname)
		print('Возраст:', acc_age)
		print('Страна:', acc_country)
		print('Язык:', acc_language)
		print('Счёт:', acc_cash)
		f.close()
		gg = input('1)Далее 2)Назад')
		if gg == '2':
			self.actions()
	def edit_profile(self):
		выбор_изменения = input('''1)Изменить имя(и фамилию)
2)Изменить возраст
3)Изменить страну
4)Изменить язык\n>>>''')
		if выбор_изменения == '1':
			############################## Супер конструкция
			f = open(self.login,"r")
			acc_list = f.read()
			acc_list2 = acc_list.split("'")
			acc_list2[3] = input('Имя: ')
			acc_list2[5] = input('Фамилия: ')
			acc_list2 = "'".join(acc_list2)
			f.close()
			f = open(self.login,"w")
			f.write(str(acc_list2))
			f.close()
			############################## Супер конструкция
		elif выбор_изменения == '2':
			f = open(self.login,"r")
			acc_list = f.read()
			acc_list2 = acc_list.split("'")
			acc_list2[7] = input('Возраст: ')
			acc_list2 = "'".join(acc_list2)
			f.close()
			f = open(self.login,"w")
			f.write(str(acc_list2))
			f.close()
		elif выбор_изменения == '3':
			f = open(self.login,"r")
			acc_list = f.read()
			acc_list2 = acc_list.split("'")
			acc_list2[9] = input('Страна: ')
			acc_list2 = "'".join(acc_list2)
			f.close()
			f = open(self.login,"w")
			f.write(str(acc_list2))
			f.close()
		elif выбор_изменения == '4':
			f = open(self.login,"r")
			acc_list = f.read()
			acc_list2 = acc_list.split("'")
			acc_list2[11] = input('Язык: ')
			acc_list2 = "'".join(acc_list2)
			f.close()
			f = open(self.login,"w")
			f.write(str(acc_list2))
			f.close()
		print("===============Профиль успешно изменён===============А")
def work():
	try:
		choice = input('''1)Войти
2)Регистрация\n>>>''')
		if choice == '1':
			os.system('cls')
			print("===============Авторизация===============")
			user = Users(input("Введите логин:"), input("Введите пароль:"), None, None, None, None, None, None)
			user.enter()
		elif choice == '2':
			os.system('cls')
			print("===============Регистрация===============")
			user = Users(input("Придумайте логин:"), input("Придумайте пароль:"), input('Ваше имя:'), input('Фамилия:'), input('Возраст:'), input('Страна, где вы живёте:'), input('Ваш язык:'), '5000')
			user.regist()
	except FileNotFoundError:
		os.system('cls')
		print('Такого пользователя не существует')
		выбор2 = input('1)Попробовать ещё\
2)Зарегестрировать пользователя\n>>>')
		if выбор2 == '1':
			os.system('cls')
			user = Users(input("Введите логин:"), input("Введите пароль:"), None, None, None, None, None, None)
			user.enter()
		elif выбор2 == '2':
			os.system('cls')
			print("===============Регистрация===============")
			user = Users(input("Придумайте логин:"), input("Придумайте пароль:"), input('Ваше имя:'), input('Фамилия:'), input('Возраст:'), input('Страна, где вы живёте:'), input('Ваш язык:'), '5000')
			user.regist()
def buying(login): #Блок покупок
	os.system('cls')
	f = open(login, 'r')
	acc_list = f.read()
	acc_list = acc_list.split("'")
	acc_cash = acc_list[13]
	acc_cash = int(acc_cash)
	f.close()
	print('''===============Магазин===============''','\nВаш счёт:', acc_cash,'''
Список доступных товаров:
1)-1000
2)-900
3)-800
4)-700
5)-500
6)-400
7)-300
8)-200
9)-100''')
	выбор_покупки = input('>>>')
	if выбор_покупки == "1":
		############################## Супер конструкция списания денег
		f = open(login, 'r')
		acc_list = f.read()
		acc_list = acc_list.split("'")
		acc_cash = acc_list[13]
		acc_cash = int(acc_cash)
		country_me = str(acc_list[9])
		acc_cash -= 1000 #<---Менять надо это;)
		acc_list[13] = str(acc_cash)
		acc_list3 = "'".join(acc_list)
		f.close()
		f = open(login, 'w')
		f.write(str(acc_list3))
		f.close()
		############################## Супер конструкция
		print('Покупка...')
		time.sleep(3)
		print('Покупка успешно произведена.')
		print('На Вашем счету осталось: ', acc_cash, 'р')
		while True:
			очередной_выбор = input('1)Ещё 2)Для выхода нажмите ENTER')
			if очередной_выбор == '1':
				buying(login)
			elif очередной_выбор == '':
				break
	elif выбор_покупки == "2":
		############################## Супер конструкция списания денег
		f = open(login, 'r')
		acc_list = f.read()
		acc_list = acc_list.split("'")
		acc_cash = acc_list[13]
		acc_cash = int(acc_cash)
		country_me = str(acc_list[9])
		acc_cash -= 900 #<---Менять надо это;)
		acc_list[13] = str(acc_cash)
		acc_list3 = "'".join(acc_list)
		f.close()
		f = open(login, 'w')
		f.write(str(acc_list3))
		f.close()
		############################## Супер конструкция
		print('Покупка...')
		time.sleep(3)
		print('Покупка успешно произведена.')
		print('На Вашем счету осталось: ', acc_cash  ,'р')
		while True:
			очередной_выбор = input('1)Ещё 2)Для выхода нажмите ENTER')
			if очередной_выбор == '1':
				buying(login)
			elif очередной_выбор == '':
				break
	elif выбор_покупки == "3":
		############################## Супер конструкция списания денег
		f = open(login, 'r')
		acc_list = f.read()
		acc_list = acc_list.split("'")
		acc_cash = acc_list[13]
		acc_cash = int(acc_cash)
		country_me = str(acc_list[9])
		acc_cash -= 800 #<---Менять надо это;)
		acc_list[13] = str(acc_cash)
		acc_list3 = "'".join(acc_list)
		f.close()
		f = open(login, 'w')
		f.write(str(acc_list3))
		f.close()
		############################## Супер конструкция
		print('Покупка...')
		time.sleep(3)
		print('Покупка успешно произведена.')
		print('На Вашем счету осталось: ', acc_cash  ,'р')
		while True:
			очередной_выбор = input('1)Ещё 2)Для выхода нажмите ENTER')
			if очередной_выбор == '1':
				buying(login)
			elif очередной_выбор == '':
				break
	elif выбор_покупки == "4":
		############################## Супер конструкция списания денег
		f = open(login, 'r')
		acc_list = f.read()
		acc_list = acc_list.split("'")
		acc_cash = acc_list[13]
		acc_cash = int(acc_cash)
		country_me = str(acc_list[9])
		acc_cash -= 800 #<---Менять надо это;)
		acc_list[13] = str(acc_cash)
		acc_list3 = "'".join(acc_list)
		f.close()
		f = open(login, 'w')
		f.write(str(acc_list3))
		f.close()
		############################## Супер конструкция
		print('Покупка...')
		time.sleep(3)
		print('Покупка успешно произведена.')
		print('На Вашем счету осталось: ', acc_cash  ,'р')
		
		while True:
			очередной_выбор = input('1)Ещё 2)Для выхода нажмите ENTER')
			if очередной_выбор == '1':
				buying(login)
			elif очередной_выбор == '':
				break
	elif выбор_покупки == "5":
		############################## Супер конструкция списания денег
		f = open(login, 'r')
		acc_list = f.read()
		acc_list = acc_list.split("'")
		acc_cash = acc_list[13]
		acc_cash = int(acc_cash)
		country_me = str(acc_list[9])
		acc_cash -= 500 #<---Менять надо это;)
		acc_list[13] = str(acc_cash)
		acc_list3 = "'".join(acc_list)
		f.close()
		f = open(login, 'w')
		f.write(str(acc_list3))
		f.close()
		############################## Супер конструкция
		print('Покупка...')
		time.sleep(3)
		print('Покупка успешно произведена.')
		print('На Вашем счету осталось: ', acc_cash  ,'р')
		while True:
			очередной_выбор = input('1)Ещё 2)Для выхода нажмите ENTER')
			if очередной_выбор == '1':
				buying(login)
			elif очередной_выбор == '':
				break
	elif выбор_покупки == "6":
		############################## Супер конструкция списания денег
		f = open(login, 'r')
		acc_list = f.read()
		acc_list = acc_list.split("'")
		acc_cash = acc_list[13]
		acc_cash = int(acc_cash)
		country_me = str(acc_list[9])
		acc_cash -= 400 #<---Менять надо это;)
		acc_list[13] = str(acc_cash)
		acc_list3 = "'".join(acc_list)
		f.close()
		f = open(login, 'w')
		f.write(str(acc_list3))
		f.close()
		############################## Супер конструкция
		print('Покупка...')
		time.sleep(3)
		print('Покупка успешно произведена.')
		print('На Вашем счету осталось: ', acc_cash  ,'р')
		while True:
			очередной_выбор = input('1)Ещё 2)Для выхода нажмите ENTER')
			if очередной_выбор == '1':
				buying(login)
			elif очередной_выбор == '':
				break
	elif выбор_покупки == "7":
		############################## Супер конструкция списания денег
		f = open(login, 'r')
		acc_list = f.read()
		acc_list = acc_list.split("'")
		acc_cash = acc_list[13]
		acc_cash = int(acc_cash)
		country_me = str(acc_list[9])
		acc_cash -= 700 #<---Менять надо это;)
		acc_list[13] = str(acc_cash)
		acc_list3 = "'".join(acc_list)
		f.close()
		f = open(login, 'w')
		f.write(str(acc_list3))
		f.close()
		############################## Супер конструкция
		print('Покупка...')
		time.sleep(3)
		print('Покупка успешно произведена.')
		print('На Вашем счету осталось: ', acc_cash  ,'р')
		while True:
			очередной_выбор = input('1)Ещё 2)Для выхода нажмите ENTER')
			if очередной_выбор == '1':
				buying(login)
			elif очередной_выбор == '':
				break
	elif выбор_покупки == "8":
		############################## Супер конструкция списания денег
		f = open(login, 'r')
		acc_list = f.read()
		acc_list = acc_list.split("'")
		acc_cash = acc_list[13]
		acc_cash = int(acc_cash)
		country_me = str(acc_list[9])
		acc_cash -= 200 #<---Менять надо это;)
		acc_list[13] = str(acc_cash)
		acc_list3 = "'".join(acc_list)
		f.close()
		f = open(login, 'w')
		f.write(str(acc_list3))
		f.close()
		############################## Супер конструкция
		print('Покупка...')
		time.sleep(3)
		print('Покупка успешно произведена.')
		print('На Вашем счету осталось: ', acc_cash  ,'р')
		while True:
			очередной_выбор = input('1)Ещё 2)Для выхода нажмите ENTER')
			if очередной_выбор == '1':
				buying(login)
			elif очередной_выбор == '':
				break
	elif выбор_покупки == "9":
		############################## Супер конструкция списания денег
		f = open(login, 'r')
		acc_list = f.read()
		acc_list = acc_list.split("'")
		acc_cash = acc_list[13]
		acc_cash = int(acc_cash)
		country_me = str(acc_list[9])
		acc_cash -= 100 #<---Менять надо это;)
		acc_list[13] = str(acc_cash)
		acc_list3 = "'".join(acc_list)
		f.close()
		f = open(login, 'w')
		f.write(str(acc_list3))
		f.close()
		############################## Супер конструкция
		print('Покупка...')
		time.sleep(3)
		print('Покупка успешно произведена.')
		print('На Вашем счету осталось: ', acc_cash  ,'р')
		while True:
			очередной_выбор = input('1)Ещё 2)Для выхода нажмите ENTER')
			if очередной_выбор == '1':
				buying(login)
			elif очередной_выбор == '':
				break
def work_again():
	try:
		choice = input('''1)Попробовать ещё раз
2)Зарегестрировать пользователя
3)Обновить пароль\n>>>''')
		if choice == '1':
			os.system('cls')
			print("===============Авторизация===============")
			user = Users(input("Введите логин:"), input("Введите пароль:"), None, None, None, None, None, None)
			user.enter()
		elif choice == '2':
			os.system('cls')
			print("===============Регистрация===============")
			user = Users(input("Придумайте логин:"), input("Придумайте пароль:"), input('Ваше имя:'), input('Фамилия:'), input('Возраст:'), input('Страна, где вы живёте:'), input('Ваш язык:'), '5000')
			user.regist()
		elif choice == '3':
			os.system('cls')
			logg = input("Введите логин ещё раз:")
			f = open(logg,"r")
			acc_list = f.read()
			acc_list = acc_list.split("'")
			user = Users(logg,input("Придумайте пароль:"),acc_list[3],acc_list[5],acc_list[7],acc_list[9],acc_list[11])
			user.regist()
	except FileNotFoundError:
		os.system('cls')
		print('Такого пользователя не существует')
		выбор2 = input('''1)Попробовать ещё
2)Зарегестрировать пользователя\n>>>''')
		if выбор2 == '1':
			user = Users(input("Введите логин:"), input("Введите пароль:"), None, None, None, None, None, None)
			user.enter()
		elif выбор2 == '2':
			print("===============Регистрация===============")
			user = Users(input("Придумайте логин:"), input("Придумайте пароль:"), input('Ваше имя:'), input('Фамилия:'), input('Возраст:'), input('Страна, где вы живёте:'), input('Ваш язык:'), '5000')
			user.regist()
work()
