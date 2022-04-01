import mysql.connector

koneksi = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_py'
)

my_cursor = koneksi.cursor()
my_cursor.execute("CREATE TABLE tb_py (id INT AUTO_INCREMENT PRIMARY KEY, nama VARCHAR(255), umur VARCHAR(255))")
if my_cursor:
    print('berhasil membuat table tb_py')
else:
    print('gagal membuatt table tb_py')