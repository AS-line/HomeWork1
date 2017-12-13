import sqlite3


def registration():
	descriptor = sqlite3.connect('DATA.db')
	runner = descriptor.cursor()

	idmeter = open("fileid", "r")
	usid = idmeter.read()
	usid += '1'
	idmeter.close()
	idmeter = open('fileid', 'w')
	idmeter.write(str(usid))
	idmeter.close()

	query = "INSERT INTO profiles_data VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
	date = usid, input('name:'), input('sername: '), input('language: '), input('age: '), input('country: '), input("login: "), input("passworld: ")
	runner.execute(query, date)

	descriptor.commit()
	runner.close()
	descriptor.close()
	print("YOU HAVE SUCCESSFULLY REGISTERED")

def log_in():
	descriptor = sqlite3.connect('DATA.db')
	runner = descriptor.cursor()

	runner.execute("SELECT login, passworld FROM profiles_data")
	profiles = runner.fetchall()
	true_login = input('login: ')
	check_profile = (true_login, input('passworld: '))
	if check_profile in profiles:
		print('YOU HAVE SUCCESSFULLY LOGGED')
		input("GO TO MENU")
		actions()
	else:
		print('INCORRECT USERNAME OR PASSWORD')
		выбор = input('TRY AGAIN?\n1)Y\n2)N\n')
		if выбор == '1':
			log_in()

	descriptor.commit()
	runner.close()
	descriptor.close()

def actions():
	print("MENU")
	выбор = input('1)SHOW MY PROFILE\n2)EXIT\n')
	if выбор == '1':
		show_profile()

def show_profile():
	descriptor = sqlite3.connect('DATA.db')
	runner = descriptor.cursor()

	runner.execute("SELECT name, sername, language, age, country FROM profiles_data WHERE login = true_login")
	profile_data = runner.fetchall()
	print(profile_data)






def start():
	выбор = input('1)REG\n2)LOGIN\n')
	if выбор == '1':
		registration()
	elif выбор == '2':
		log_in()




start()
