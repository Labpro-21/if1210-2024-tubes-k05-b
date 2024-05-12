import parseran
def Help() -> None:
    user_login=parseran.read_csv('user_login.csv')
    data_role=user_login[1][2]
    data_username=user_login[1][1]
    data_status_login=user_login[1][4]
    if data_status_login=="False":
        print("=========== HELP ===========")
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print("1. Login: Masuk ke dalam akun yang sudah terdaftar")
        print("2. Register: Membuat akun baru")
        print("Footnote:")
        print("1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
        print("2. Jangan lupa untuk memasukkan input yang valid")
    elif data_role=="Agent":
        print(f"Halo Agent {data_username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian.")
        print("============ HELP ============")
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. logout - Untuk melakukan logout pada sistem")
        print("3. inventory - Untuk melihat jumlah O.W.C.A Coin, monster, dan potion yang dimiliki")
        print("4. battle - Untuk bertarung melawan monster secara random")
        print("5. arena - Untuk melatih monster yang dimiliki dan mendapatkan hadiah berupa O.W.C.A Coin")
        print("6. shop_currency - Untuk membeli monster dan potion pada toko")
        print("7. laboratory - Untuk melakukan upgrade monster yang dimiliki di inventory")
        print("8. save - Untuk melakukan penyimpanan data")
        print("9. exit - Untuk keluar dari program")
        print("\n")
        print("Footnote:")
        print('1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar')
        print('2. Jangan lupa untuk memasukkan input yang valid')
    elif data_role=="Admin":
        print('Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:') 
        print("============ HELP ============")
        print("1. register - Untuk melakukan registrasi user baru")
        print("2. login - Untuk melakukan login ke dalam sistem")
        print("3. logout - Untuk melakukan logout pada sistem")
        print("4. shop_management - Untuk melakukan penambahan, perubahan, dan penghapusan Item yang dijual dari Database, pengaturan harga dan jumlah dari tiap item pada toko")
        print("5. monster_management - Untuk mengatur dan menambahkan data monster dalam database")
        print("6. save - Untuk melakukan penyimpanan data")
        print("7.  exit - Untuk keluar dari program")
        print("\n")
        print("Footnote:")
        print("1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
        print("2. Jangan lupa untuk memasukkan input yang valid")