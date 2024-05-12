import parseran 
import Shop_Currency
import buat_shop
monster_shop=parseran.read_csv('monster_shop.csv')
monster_inv=parseran.read_csv('monster_inventory.csv')
item_inv=parseran.read_csv('item_inventory.csv')
item_shop=parseran.read_csv('item_shop.csv')
monster = parseran.read_csv('monster.csv')
shop_m = buat_shop.load_data_m_shop_buat_shop_c()
shop_p = buat_shop.load_data_p_shop_buat_shop_c()

def cari_yg_gk_ada(a:list,b:list)->list:
    c=[]
    idx = 0
    for i in a:
        if i != b[idx]:
            c.append(i)
        else:
            idx += 1
        if idx > len(b) - 1:
            idx = len(b)-1
    return c
#semua yang ada di monster.csv diliatin. tapi yg gk ada stoknya doang
#cari dulu yang ada di monster.csv tapi gak ada di monster_shop
def tambah_m():
    monster_shop=parseran.read_csv('monster_shop.csv')
    monster_inv=parseran.read_csv('monster_inventory.csv')
    monster = parseran.read_csv('monster.csv')
    a = [monster[i][0] for i in range(1,len(monster))]
    b = [monster_shop[i][0] for i in range(1, len(monster_shop))]
    c = cari_yg_gk_ada(a,b)
    print('ID | Type     | ATK Power | DEF Power | HP  ')
    m_blm_sell=[]
    for m in monster:
        if m[0] in c:
            spasi_atk= len(' ATK Power ')-len(m[2])-1
            spasi_def= len(' DEF Power ')-len(m[3])-1
            print(f'{m[0]}  | {m[1]}    | {m[2]}' + spasi_atk*" " + f'| {m[3]}' + spasi_def*" " + f'| {m[4]}  |')
            m_blm_sell.append([m[0],m[1],m[2],m[3],m[4]])
    id=int(input('>>> Masukkan id monster: '))
    if str(id) in (m_blm_sell[0][i] for i in range(len(m_blm_sell))):
        stok_new=input('>>> Masukkan stok awal: ')
        harga_baru=input('>>> Masukkan harga: ')
        monster_shop.append([monster[id][0],stok_new,harga_baru])
        parseran.save_data('monster_shop.csv',monster_shop)
    else:
        print('id yang anda masukkan tidak valid')
def tambah_p():
    item_shop=parseran.read_csv('item_shop.csv')
    a = ['Magic','Power']
    b = [item_shop[i][1] for i in range(1, len(item_shop))]
    c = cari_yg_gk_ada(a,b)
    print('ID | Type |')
    idx=1
    for p_tambah in c:
        print(f'{idx} | {p_tambah} |')
        idx+=1
    type=input('>>> Masukkan type potion: ')
    if type in c:
        stok_new=input('>>> Masukkan stok awal: ')
        harga_baru=input('>>> Masukkan harga: ')
        item_shop.append([type,stok_new,harga_baru])
        parseran.save_data('item_shop.csv',item_shop)
    else:
        print('id yang anda masukkan tidak valid')


def ubah_m():
    monster_shop=parseran.read_csv('monster_shop.csv')
    Shop_Currency.lihat_monster()
    id=int(input('>>> Masukkan id monster: '))
    if str(id) in shop_m["id_m"]:
        stok_new=input('>>> Masukkan stok baru: ')
        harga_baru=input('>>> Masukkan harga baru: ')
        if stok_new!='':
            monster_shop[id][1]=stok_new
        if harga_baru!='':
            monster_shop[id][2]=harga_baru
        if stok_new!='' and harga_baru!='':
            print(f'{shop_m["type_m"][id-1]} telah berhasil diubah dengan stok baru sejumlah {stok_new} dan dengan harga baru {harga_baru}!')
        elif stok_new!='':
            print(f'{shop_m["type_m"][id-1]} telah berhasil diubah dengan stok baru sejumlah {stok_new}')
        elif harga_baru!='':
            print(f'{shop_m["type_m"][id-1]} telah berhasil diubah dengan harga baru {harga_baru}!')
        parseran.save_data('monster_shop.csv',monster_shop)
        return
    else:
        print(f'id {id} tidak terdapat di dalam monster_shop.csv')
        return


def ubah_p():
    item_shop=parseran.read_csv('item_shop.csv')
    Shop_Currency.lihat_potion()
    shop_m = buat_shop.load_data_m_shop_buat_shop_c()
    id=int(input('>>> Masukkan id potion: '))
    if str(id) in shop_p["id_p"]:
        stok_new=input('>>> Masukkan stok baru: ')
        harga_baru=input('>>> Masukkan harga baru: ')
        if stok_new!='':
            item_shop[id][1]=stok_new
        if harga_baru!='':
            item_shop[id][2]=harga_baru
        if stok_new!='' and harga_baru!='':
            print(f'{shop_p["type_p"][id-1]} telah berhasil diubah dengan stok baru sejumlah {stok_new} dan dengan harga baru {harga_baru}!')
        elif stok_new!='':
            print(f'{shop_p["type_p"][id-1]} telah berhasil diubah dengan stok baru sejumlah {stok_new}')
        elif harga_baru!='':
            print(f'{shop_p["type_p"][id-1]} telah berhasil diubah dengan harga baru {harga_baru}!')
        parseran.save_data('item_shop.csv',item_shop)
        return
    else:
        print(f'id {id} tidak terdapat di dalam item_shop.csv')
        return
    

#harus apus satu baris, terus baris yang dibawahnya dinaikin(klo misal yg dihapus di tengah) klo yg diapus di akhir biarin aja
def hapus_m():
    Shop_Currency.lihat_monster()
    shop_m = buat_shop.load_data_m_shop_buat_shop_c()
    monster_shop=parseran.read_csv('monster_shop.csv')
    id=int(input('>>> Masukkan id monster: '))
    found=False
    for i in range(len(shop_m["id_m"])):
        if id==int(shop_m["id_m"][i]):
            save_i=i
            found=True
    if found:
        yakin_apus=input(f'>>> Apakah anda yakin ingin menghapus {shop_m["type_m"][save_i]} dari shop (y/n)? ')
        if yakin_apus=='y':
            monster_shop_e=parseran.matrix_pop(monster_shop,[monster_shop[save_i+1][0],monster_shop[save_i+1][1],monster_shop[save_i+1][2]])
            parseran.save_data('monster_shop.csv',monster_shop_e)
        else:
            print(f'Anda tidak jadi hapus monster dengan ID {id}')
    else:
        print(f'id {id} tidak ditemukan')

def hapus_p():
    Shop_Currency.lihat_potion()
    item_shop=parseran.read_csv('item_shop.csv')
    id=int(input('>>> Masukkan id potion: '))
    found=False
    for i in range(len(shop_p["id_p"])):
        if id==int(shop_p["id_p"][i]):
            found=True
            save_i=i+1
            break
    print(save_i)
    if found:
        yakin_apus=input(f'>>> Apakah anda yakin ingin menghapus {shop_p["type_p"][id-1]} Potion dari shop (y/n)? ')
        if yakin_apus=='y':
            item_shop_e=parseran.matrix_pop(item_shop,[item_shop[save_i][0],item_shop[save_i][1],item_shop[save_i][2]])
            parseran.save_data('item_shop.csv',item_shop_e)
        else:
            print(f'Anda tidak jadi hapus monster dengan ID {id}')
    else:
        print(f'Anda tidak jadi hapus potion dengan ID {id}')

def shop_management():
    print('Irasshaimase! Selamat datang kembali, Mr. Monogram!')
    pilihan=input('>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ')
    while pilihan!='keluar':
        if pilihan=='lihat':
            lihat_apa=input('>>> Mau lihat apa? (monster/potion): ')
            if lihat_apa=='monster':
                Shop_Currency.lihat_monster()
            elif lihat_apa=='potion':
                Shop_Currency.lihat_potion()
        elif pilihan=='tambah':
            tambah_apa=input('>>> Mau nambahin apa? (monster/potion): ')
            if tambah_apa=='monster':
                tambah_m()
            elif tambah_apa=='potion':
                tambah_p()
        elif pilihan=='ubah':
            ubah_apa=input('>>> Mau ubah apa? (monster/potion): ')
            if ubah_apa=='monster':
                ubah_m()
            elif ubah_apa=='potion':
                ubah_p()
        elif pilihan=='hapus':
            hapus_apa=input('>>> Mau hapus apa? (monster/potion): ')
            if hapus_apa=='monster':
                hapus_m()
            elif hapus_apa=='potion':
                hapus_p()
        pilihan=input('>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ')
    print('Dadah Mr. Yanto, sampai jumpa lagi!')
shop_management()