import parseran
import Shop_Currency
import buat_shop
from Shop_Currency import change_type_id
def bubble_sort(arr:list):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def cari_yg_gk_ada(a: list, b: list) -> list:
    c = []
    idx = 0
    for i in a:
        if i == b[idx]:
            if idx < len(b)-1:
                idx += 1
        else:
            c.append(i)
    return c

def check_m_in_shop(shop_m:dict,id:int)->(int,bool):
    found=False
    for i in range(len(shop_m["id_m"])):
        if id==int(shop_m["id_m"][i]):
            save_i=i
            found=True
    return (save_i,found)

def check_p_in_shop(shop_p:dict,type:str)->(int,bool):
    found=False
    save_i=0
    for i in range(len(shop_p["id_p"])):
        if type==shop_p["type_p"][i]:
            found=True
            save_i=i+1
            break
    return (save_i,found)
#semua yang ada di monster.csv diliatin. tapi yg gk ada stoknya doang
#cari dulu yang ada di monster.csv tapi gak ada di monster_shop
def tambah_m(monster:list,monster_shop:list)->list:
    a = bubble_sort(change_type_id([monster[i][0] for i in range(1,len(monster))]))
    b = bubble_sort(change_type_id([monster_shop[i][0] for i in range(1, len(monster_shop))]))
    c = cari_yg_gk_ada(a,b)
    print('ID | Type     | ATK Power | DEF Power | HP  ')
    m_blm_sell=[]
    for m in monster:
        if m[0] in str(c):
            spasi_atk= len(' ATK Power ')-len(m[2])-1
            spasi_def= len(' DEF Power ')-len(m[3])-1
            print(f'{m[0]}  | {m[1]}    | {m[2]}' + spasi_atk*" " + f'| {m[3]}' + spasi_def*" " + f'| {m[4]}  |')
            m_blm_sell.append([m[0],m[1],m[2],m[3],m[4]])
    id=int(input('>>> Masukkan id monster: '))
    if str(id) in (m_blm_sell[0][i] for i in range(len(m_blm_sell))):
        stok_new=input('>>> Masukkan stok awal: ')
        harga_baru=input('>>> Masukkan harga: ')
        monster_shop.append([monster[id][0],stok_new,harga_baru])
    else:
        print('id yang anda masukkan tidak valid')
    return monster_shop
def tambah_p(item_shop:list)->list:
    a = ['magic','power', 'strength', 'resilience', 'healing']
    b = [item_shop[i][0] for i in range(1, len(item_shop))]
    print(b)
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
    else:
        print('type yang anda masukkan tidak valid')
    return item_shop


def ubah_m(monster_shop:list,monster:list)->list:
    Shop_Currency.lihat_monster(monster_shop,monster)
    shop_m = buat_shop.load_data_m_shop_buat_shop_c(monster,monster_shop)
    id=int(input('>>> Masukkan id monster: '))
    (save_i,found)=check_m_in_shop(shop_m,id)
    if found:
        stok_new=input('>>> Masukkan stok baru: ')
        harga_baru=input('>>> Masukkan harga baru: ')
        if stok_new!='':
            monster_shop[save_i+1][1]=stok_new
        if harga_baru!='':
            monster_shop[save_i+1][2]=harga_baru
        if stok_new!='' and harga_baru!='':
            print(f'{shop_m["type_m"][save_i]} telah berhasil diubah dengan stok baru sejumlah {stok_new} dan dengan harga baru {harga_baru}!')
        elif stok_new!='':
            print(f'{shop_m["type_m"][save_i]} telah berhasil diubah dengan stok baru sejumlah {stok_new}')
        elif harga_baru!='':
            print(f'{shop_m["type_m"][save_i]} telah berhasil diubah dengan harga baru {harga_baru}!')
    else:
        print(f'id {id} tidak ditemukan')
    return monster_shop

def ubah_p(item_shop:list)->list:
    Shop_Currency.lihat_potion(item_shop)
    shop_p = buat_shop.load_data_p_shop_buat_shop_c(item_shop)
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
    else:
        print(f'id {id} tidak terdapat di dalam item_shop.csv')
    return item_shop
    

#harus apus satu baris, terus baris yang dibawahnya dinaikin(klo misal yg dihapus di tengah) klo yg diapus di akhir biarin aja
def hapus_m(monster_shop:list,monster:list)->list:
    Shop_Currency.lihat_monster(monster_shop,monster)
    shop_m = buat_shop.load_data_m_shop_buat_shop_c(monster,monster_shop)
    id=int(input('>>> Masukkan id monster: '))
    (save_i,found)=check_m_in_shop(shop_m,id)
    if found:
        yakin_apus=input(f'>>> Apakah anda yakin ingin menghapus {shop_m["type_m"][save_i]} dari shop (y/n)? ')
        if yakin_apus=='y':
            print(f'Yey, anda berhasil menghapus monste {shop_m["type_m"][save_i]}')
            monster_shop=parseran.matrix_pop(monster_shop,[monster_shop[save_i+1][0],monster_shop[save_i+1][1],monster_shop[save_i+1][2]])
        else:
            print(f'Anda tidak jadi hapus monster dengan ID {id}')
    else:
        print(f'id {id} tidak ditemukan')
    return monster_shop

def hapus_p(item_shop:list)->list:
    Shop_Currency.lihat_potion(item_shop)
    shop_p = buat_shop.load_data_p_shop_buat_shop_c(item_shop)
    type=input('>>> Masukkan type potion: ')
    (save_i,found)=check_p_in_shop(shop_p,type)
    if found:
        yakin_apus=input(f'>>> Apakah anda yakin ingin menghapus {shop_p["type_p"][save_i-1]} Potion dari shop (y/n)? ')
        if yakin_apus=='y':
            print(f'Yey, anda berhasil menghapus potion {shop_p["type_p"][save_i-1]}')
            item_shop=parseran.matrix_pop(item_shop,[item_shop[save_i][0],item_shop[save_i][1],item_shop[save_i][2]])
        else:
            print(f'Anda tidak jadi hapus monster dengan type {type}')
    else:
        print(f'type {type} tidak ditemukan')
    return item_shop

def shop_management(monster_shop:list,item_shop:list,monster:list):
    print('Irasshaimase! Selamat datang kembali, Mr. Monogram!')
    pilihan=input('>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ')
    while pilihan!='keluar':
        if pilihan=='lihat':
            lihat_apa=input('>>> Mau lihat apa? (monster/potion): ')
            if lihat_apa=='monster':
                Shop_Currency.lihat_monster(monster_shop,monster)
            elif lihat_apa=='potion':
                Shop_Currency.lihat_potion(item_shop)
        elif pilihan=='tambah':
            tambah_apa=input('>>> Mau nambahin apa? (monster/potion): ')
            if tambah_apa=='monster':
                monster_shop=tambah_m(monster,monster_shop)
            elif tambah_apa=='potion':
                item_shop=tambah_p(item_shop)
        elif pilihan=='ubah':
            ubah_apa=input('>>> Mau ubah apa? (monster/potion): ')
            if ubah_apa=='monster':
                monster_shop=ubah_m(monster_shop,monster)
            elif ubah_apa=='potion':
                item_shop=ubah_p(item_shop)
        elif pilihan=='hapus':
            hapus_apa=input('>>> Mau hapus apa? (monster/potion): ')
            if hapus_apa=='monster':
                monster_shop=hapus_m(monster_shop,monster)
            elif hapus_apa=='potion':
                item_shop=hapus_p(item_shop)
        pilihan=input('>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ')
    print('Dadah Mr. Yanto, sampai jumpa lagi!')
#shop_management()