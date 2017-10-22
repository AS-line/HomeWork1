import time
def trakk():
	track_choo = input('''Где гонять?
	1)Трасса(40км)

	2)Пляж(30км)

	3)Город(25км)\n''')
	if track_choo == '1':
		track = 40
	elif track_choo == '2':
		track = 30
	else:
		track = 25
	return track
track = trakk()
def tr():
	trk = track
	return trk
def ride(car):
	car['distance'] += car['speed']
	car['fuel'] -= car['spend']

def faster(car):
	car['speed'] += 2
	car['spend'] += 2

def nitro(car):
	car['distance'] += car['nitro']
	car['fuel'] -= car['spend'] * 2

def car_info(car):
	print('▬'*70 ,
		  '\n' + car['name'] + ', твоё текущее состояние' + ":" ,
		  '\n' + 'Топливо: ' + str(car['fuel']),
		  '\n' + 'Скорость: ' + str(car['speed']),
		  '\n' + 'Проехали: ' + str(car['distance']) + '/' + str(track),
		  '\n' + '▬'*70)

def race_step(car):
	time.sleep(1)
	choose = input('\nТвой ход, ' + car['name'] + """ Что будем делать?
1)ехать
2)переключить передачу
3)дать по газам\n""")
	# print('        1')
	# time.sleep(1)
	# print('        2')
	# time.sleep(1)
	# print('        3')
	# print('        Поехали!')
	if choose == '1':
		ride(car)
	elif choose == '2':
		faster(car)
	elif choose == '3':
		nitro(car)
	car_info(car)
	time.sleep(0.1)



# racer1 = {
# 	'name': 'Чайка',
# 	'speed': 5,
# 	'fuel': 25,
# 	'spend': 2,
# 	'nitro': 8,
# 	'distance': 0
# }


# racer2 = {
# 	'name': 'Ниво',
# 	'speed': 3,
# 	'fuel': 35,
# 	'spend': 2,
# 	'nitro': 6,
# 	'distance': 0
# }


# racer3 = {
# 	'name': 'Шиха',
# 	'speed': 6,
# 	'fuel': 30,
# 	'spend': 5,
# 	'nitro': 10,
# 	'distance': 0,
# }



time.sleep(1)
print('''Учавствуют 3 машины:
	Чайка
		скорость ▀▀▀▀▀ 5
		бак      ▀▀▀ 25
		нитро    ▀▀▀▀ 8
		расход   ▀▀ 2

	Ниво 
		скорость ▀▀▀ 3
		бак      ▀▀▀▀▀ 35
		нитро    ▀▀▀ 6
		расход   ▀▀▀▀ 4

	Шиха 
		скорость ▀▀▀▀ 4
		бак      ▀▀▀ 30
		нитро    ▀▀ 4
		расход   ▀▀▀ 3

''')
# track_choo = int(input('''Где гонять?
# 	1)Трасса(40км)

# 	2)Пляж(30км)

# 	3)Город(25км)\n'''))
# if track_choo == 1:
# 	track = 40
# elif track_choo == 2:
# 	track = 30
# else:
# 	track = 25
input('Press ENTER')
print('        1')
time.sleep(1)
print('        2')
time.sleep(1)
print('        3')
time.sleep(1)
print('     Поехали!')