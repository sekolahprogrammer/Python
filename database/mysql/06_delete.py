import mysql.connector

koneksi = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_py'
)

my_cursor = koneksi.cursor()

query = "DELETE FROM tb_py WHERE id='4'"
my_cursor.execute(query)

koneksi.commit()

if my_cursor:
    print('delete berhasil')
else:
    print('delete gagal')