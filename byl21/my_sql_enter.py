import sqlite3

basedata = sqlite3.connect('my_bd.db')
runner = basedata.cursor()
runner.execute('SELECT f3 FROM my_first_table')
my_output = runner.fetchall()
print(my_output)
basedata.commit()
runner.close()
basedata.close()