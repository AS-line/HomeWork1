import sqlite3

basedata = sqlite3.connect('my_bd.db')
runner = basedata.cursor()

runner.execute('DROP TABLE my_first_table')

runner.execute("""CREATE TABLE my_first_table (
	f1 VARCHAR(20) PRIMARY KEY,
	f2 INT,
	f3 VARCHAR(20)
)""")

runner.execute("INSERT INTO my_first_table VALUES('Это первая ячейка',2,'Это третья ячейка')")
runner.execute('INSERT INTO my_first_table VALUES(?,?,?)', ('1S2',22,'3P6'))

basedata.commit()
runner.close()
basedata.close()