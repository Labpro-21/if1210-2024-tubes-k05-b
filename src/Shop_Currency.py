from parseran import read_csv,save_data
import data
from buat_shop import load_data_m_shop_buat_shop_c,load_data_p_shop_buat_shop_c
monster_shop=read_csv('monster_shop.csv')
item_shop=read_csv('item_shop.csv')
monster =read_csv('monster.csv')
monster_inventory =read_csv('monster_inventory.csv')
item_inventory =read_csv('item_inventory.csv')

shop_m = load_data_m_shop_buat_shop_c()
shop_p = load_data_p_shop_buat_shop_c()

def lihat_monster():
    print('ID | Type           | ATK Power | DEF Power | HP   | Stok | Harga')
    for i in range(len(monster_shop)):
        if i==len(monster_shop)-1:
            break
        print(f"{shop_m['id_m'][i]}  | {shop_m['type_m'][i]}          | {shop_m['atk_m'][i]} | {shop_m['def_m'][i]} | {shop_m['hp_m'][i]}   | {shop_m['stok_m'][i]} | {shop_m['harga_m'][i]}")

def lihat_potion():
    print('ID | Type                | Stok | Harga')
    for i in range(len(item_shop)):
        if i==len(item_shop)-1:
            break
        print(f"{shop_p['id_p'][i]}  | {shop_p['type_p'][i]}                | {shop_p['stok_p'][i]} | {shop_p['harga_p'][i]}")

def beli_monster(id_m:int):
    #mengecek kepemilikan monster
    for i in range(len(monster_inventory)):
        if monster_inventory[i][1]==str(id_m):
            print(f'Monster {monster[i][1]} sudah ada dalam inventory-mu! Pembelian dibatalkan.')
            return
    if data.oc < int(monster_shop[id_m][2]):
        print('OC-mu tidak cukup.')
        return
    if monster_shop[id_m][1]=='0':
        print('Stok Monster tersebut sudah habis!')
        return
    #mngurangi stok monster di monster_shop
    monster_shop[id_m][1]=str(int(monster_shop[id_m][1])-1)
    #mengurangi oc koin
    data.oc -= int(monster_shop[id_m][2])
    #menyimpan data di monster_inventory
    new_monster =[data.id,monster[id_m][0],'1']
    monster_inventory.append(new_monster)
    save_data('monster_inventory.csv',monster_inventory)
    save_data('monster_shop.csv',monster_shop)
    print(f'Berhasil membeli item: {monster[id_m][1]}. Item sudah masuk ke inventory-mu')

def beli_potion(id_p:int, qty:int):
    if data.oc < qty*int(item_shop[id_p][2]):
        print('OC-mu tidak cukup.')
        return
    if monster_shop[id_p][1]=='0':
        print('Stok Potion tersebut sudah habis!')
        return
    #cek potion dah ada atau belum, kalau ada stok tambah, klo gk ada buat line baru
    cek_punya=False
    for i in range(len(item_inventory)):
        if item_inventory[i][1]==item_shop[id_p][0]:
            cek_punya=True
    if cek_punya:
        item_inventory[id_p][2]=str(int(item_inventory[id_p][2])+qty)
    else:
        new_potion=[data.id,item_shop[id_p][0],qty]
        item_inventory.append(new_potion)
        save_data('item_inventory.csv',item_inventory)
    #mngurangi stok potion di item_shop
    item_shop[id_p][1]=str(int(item_shop[id_p][1])-qty)
    #mengurangi oc koin
    data.oc -= 2*int(item_shop[id_p][2])
    save_data('item_shop.csv',item_shop)
    print(f'Berhasil membeli item: {qty} {item_shop[id_p][0]}. Item sudah masuk ke inventory-mu')
    

def shop_currency():
    print('Irasshaimase! Selamat datang di SHOP!!')
    pilihan=input('>>> Pilih aksi (lihat/beli/keluar): ')    
    while pilihan!='keluar':
        if pilihan=='lihat':
            lihat_apa=input('>>> Mau lihat apa? (monster/potion): ')
            if lihat_apa=='monster':
                lihat_monster()
            elif lihat_apa=='potion':
                lihat_potion()
        elif pilihan=='beli':
            beli_apa = input('>>> Mau beli apa? (monster/potion): ')
            if beli_apa=='monster':
                id_monst = int(input('>>> Masukkan id monster: '))
                beli_monster(id_monst)
            elif beli_apa=='potion':
                id_pot = int(input('>>> Masukkan id potion: '))
                qty = int(input(' Masukkan jumlah: '))
                beli_potion(id_pot,qty)
        pilihan=input('>>> Pilih aksi (lihat/beli/keluar): ')  
    print('Mr. Yanto bilang makasih, belanja lagi ya nanti :)')
"""
nanti kita ngurang2instok
validasi owca koin
nambahin data ke monster.csv

"""