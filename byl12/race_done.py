import race

racer1 = {
	'name': 'Чайка',
	'speed': 5,
	'fuel': 25,
	'spend': 2,
	'nitro': 8,
	'distance': 0
}


racer2 = {
	'name': 'Ниво',
	'speed': 3,
	'fuel': 35,
	'spend': 4,
	'nitro': 6,
	'distance': 0
}


racer3 = {
	'name': 'Шиха',
	'speed': 4,
	'fuel': 30,
	'spend': 3,
	'nitro': 4,
	'distance': 0,
}
track = race.tr()
while True:
	race.race_step(racer1)
	race.race_step(racer2)
	race.race_step(racer3)
	if racer1['fuel'] <= 0:
		print('У Чайки высох бак!')
		break
	elif racer2['fuel'] <= 0:
		print('У Нива нечего сжигать!')
		break
	elif racer3['fuel'] <= 0:
		print('Шиха засох!')
		break
	elif racer1['distance'] >= track:
		print('Чай доcтиг таргета!')
		print('Остальные глотают пыль!')
		break
	elif racer2['distance'] >= track:
		print('Ниво пьет пиво!')
		print('Остальные пьют сироп!')
		break
	elif racer3['distance'] >= track:
		print('Шиха становится Шефом!')
		print('Остальные - шестёрки!')
		break