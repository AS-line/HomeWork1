import sqlite3

descriptor = sqlite3.connect('db_file.db')
runner = descriptor.cursor()

# runner.execute("SELECT login FROM my_table")
# table = runner.fetchall()
# print(table)
runner.execute("SELECT * FROM my_table")
table = runner.fetchall()
for i in table:
	print(i[0])
# print(table)

descriptor.commit()
runner.close()
descriptor.close()