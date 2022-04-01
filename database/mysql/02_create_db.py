import mysql.connector

koneksi = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    # database='nama-database'
)

my_cursor = koneksi.cursor()
my_cursor.execute("CREATE DATABASE db_py")
if my_cursor:
    print('berhasil membuat databse db_py')
else:
    print('gagal membuat database db_py')