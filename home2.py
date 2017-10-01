import time
score = 0
print('Приветствую вас в мини-викторине. Здесь вы должны ответить на пару вопросов,')
print('введя правильный ответ.')
print(' После прохождения викторины вам будет сказано кол-во набранных очков')
print('Первый вопрос--->В каком году запущена ВИКИПЕДИЯ?')
q1 = int(input('Ответ: '))
if q1 == 2001:
	score += 1
else:
	score -= 1
print('далее...')
time.sleep(1)
print('Второй вопрос--->Какой термин ввел Раффи Арсланбеков?')
q2 = str(input('Ответ: '))
if q2 == 'Рунет' or 'рунет':
	score += 1
else:
	score -= 1
print('далее...')
time.sleep(1)
print('Третий вопрос--->В каком году была основана кампания Google Ink?')
q3 = int(input('Ответ: '))
if q3 == 1998:
	score += 1
else:
	score -= 1
print('далее...')
time.sleep(1)
print('Четвёртый вопрос--->Кто придумал язык HTML?')
q4 = str(input('Ответ: '))
if q4 == "Бернерс-ли" or 'Тим Бернерс-ли':
	score +=1
else:
	score -=1
print('далее...')
time.sleep(1)	
print('Пятый вопрос--->В каком году появился первый рекламный баннер?')
q5 = int(input('Ответ: '))
if q5 == 1994:
	score +=1
else:
	score -=1
print('далее...')
time.sleep(1)
print('Шестой вопрос--->Какой самый популярный формат для хранения растровых изображений.')
q6 = str(input("Ответ: "))
if q6 == 'JPEG' or 'JPG' or 'jpg' or 'jpeg':
	score +=1
else:
	score -=1
print('далее...')
time.sleep(1)
print('Седьмой вопрос--->Как передавались данные между компьютерами до появления сети Интернет?')
q7 = str(input('Ответ: '))
if q7 == 'вручную' or 'Вручную':
	score +=1
else:
	score -=1
print('далее...')
time.sleep(1)
print('Восьмой вопрос--->Когда отмечают Международный день блога?')
q8 = str(input('Ответ: '))
if q8 == '31 Августа' or '31 августа':
	score +=1
else:
	score -=1
print('далее...')
time.sleep(1)
print('Девятый вопрос--->Какой самый популярный поисковик в мире?')
q9 = str(input('Ответ: '))
if q9 == 'Google' or 'google':
	score +=1
else:
	score -=1
print('далее...')
time.sleep(1)
print('Десятый вопрос--->Первый развлекательный сайт в России')
q10 = str(input('Ответ: '))
if q10 == 'anekdot.ru' or 'Anekdot.ru' or 'Анекдот.ру':
	score +=1
else:
	score -=1
input('Конец. Нажмите ENTER для подведения счета')
print('--->PLEASE WAIT<---')
time.sleep(3)
print('Ваш счет: ', score)
if score <= 5 :
	print('Попробуйте подучить теорию')
if 8 >= score <= 6 :
	print('Средний результат')
if score >= 9 :
	print('Поздравляем, вы прошли тест')
