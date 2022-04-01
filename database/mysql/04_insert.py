import mysql.connector

koneksi = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_py'
)

my_cursor = koneksi.cursor()

query = "INSERT INTO tb_py (nama,umur) VALUES (%s,%s)"
value = [
    ('prayogaea', 21),
    ('putriajeng', 25)
]
my_cursor.executemany(query, value)

koneksi.commit()

if my_cursor:
    print('insert berhasil')
else:
    print('insert gagal')