import parseran
monster=parseran.read_csv('monster.csv')
monster_shop=parseran.read_csv('monster_shop.csv')
monster_inv=parseran.read_csv('monster_inventory.csv')

def check_m(monster:list,type_m:str)->bool:
    found=False
    for m in monster:
        if m[1]==type_m:
            found=True
    return found
def lihat_m():
    print('ID | Type          | ATK Power | DEF Power | HP ')
    monster=parseran.read_csv('monster.csv')
    for m in monster:
        if m[0]!="id":
            spasi_atk= len(' ATK Power ')-len(m[2])-1
            spasi_def= len(' DEF Power ')-len(m[3])-1
            print(f'{m[0]}  | {m[1]}         | {m[2]}' + spasi_atk*" " + f'| {m[3]}' + spasi_def*" " + f'| {m[4]} ')

def buat_m():
    monster=parseran.read_csv('monster.csv')
    print('Memulai pembuatan monster baru')
    type_m=input('>>> Masukkan type / Nama : ')
    found=check_m(monster,type_m)
    while found==True:
        print('Nama sudah terdaftar, coba lagi!')
        found=False
        type_m=input('>>> Masukkan type / Nama : ')
        found=check_m(monster,type_m)
    atk_m=input('>>> Masukkan ATK Power (1-1000): ')
    while not(1<=int(atk_m)<=1000):
        print('Masukan anda tidak valid, coba lagi!')
        atk_m=input('>>> Masukkan ATK Power (1-1000): ')
    def_m=input('>>> Masukkan DEF Power (0-50): ')  
    while not(0<=int(def_m)<=50):
        print('DEF Power harus bernilai 0-50, coba lagi!')
        def_m=input('>>> Masukkan DEF Power (0-50): ')
    hp_m=input('>>> Masukkan HP (0-500): ')
    while not(0<=int(hp_m)<=500):
        print('HP harus bernilai 0-500, coba lagi!')
        hp_m=input('>>> Masukkan HP (0-500): ')
    print('Monster baru berhasil dibuat')
    print(f'Type : {type_m}')
    print(f'ATK Power : {atk_m}')
    print(f'DEF Power : {def_m}')
    print(f'HP : {hp_m}')
    yakin_tambah=input('>>> Tambahkan Monster ke database (Y/N) : ')
    if yakin_tambah=='Y':
        print('Monster baru telah ditambahkan!')
        monster.append([len(monster),type_m,atk_m,def_m,hp_m])
        parseran.save_data('monster.csv',monster)
    else:
        print('Monster gagal ditambahkan!')
def monster_management():
    print('SELAMAT DATANG DI DATABASE PARA MONSTER !!!')
    print('1. Tampilkan semua Monster')
    print('2. Tambah Monster baru')
    pilih=input('>>> Pilih Aksi (1/2/keluar): ')
    while pilih!='keluar':
        if pilih=='1':
            lihat_m()
        elif pilih=='2':
            buat_m()
        pilih=input('>>> Pilih Aksi (1/2/keluar): ')
#buat_m()