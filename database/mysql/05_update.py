import mysql.connector

koneksi = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_py'
)

my_cursor = koneksi.cursor()

query = "UPDATE tb_py SET nama='putriajeng', umur='25' WHERE id='4'"
my_cursor.execute(query)

koneksi.commit()

if my_cursor:
    print('update berhasil')
else:
    print('update gagal')