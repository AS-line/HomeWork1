import sqlite3
import random

descriptor = sqlite3.connect('db_file.db')
runner = descriptor.cursor()
runner.execute('''CREATE TABLE IF NOT EXISTS my_table (
	login VARCHAR(20) PRIMARY KEY,
	passord VARCHAR(20),
	ip INT
)''')
def reg(login,passord):
	i = random.randint(1, 999)
	query = 'INSERT INTO my_table VALUES (?,?,?)'
	data = login, i, passord
	runner.execute(query,data)


выбор = input('1)reg')
if выбор == '1':
	reg(input(),input())

descriptor.commit()
runner.close()
descriptor.close()