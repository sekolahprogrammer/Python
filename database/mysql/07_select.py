import mysql.connector

koneksi = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_py'
)

my_cursor = koneksi.cursor()
my_cursor.execute("SELECT * FROM tb_py")

result = my_cursor.fetchall()

for x in result:
    print(x)