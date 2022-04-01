import mysql.connector

koneksi = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    # database='nama-database'
)

if koneksi:
    print('Koneksi database berhasil')
else:
    print('Koneksi database gagal!')