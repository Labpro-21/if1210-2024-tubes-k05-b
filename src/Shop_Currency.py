import parseran
import buat_shop
monster_shop=parseran.read_csv('monster_shop.csv')
item_shop=parseran.read_csv('item_shop.csv')
monster =parseran.read_csv('monster.csv')
monster_inventory =parseran.read_csv('monster_inventory.csv')
item_inventory =parseran.read_csv('item_inventory.csv')

shop_m = buat_shop.load_data_m_shop_buat_shop_c()
shop_p = buat_shop.load_data_p_shop_buat_shop_c()

def lihat_monster():
    monster_shop=parseran.read_csv('monster_shop.csv')
    shop_m = buat_shop.load_data_m_shop_buat_shop_c()
    print('ID | Type           | ATK Power | DEF Power | HP   | Stok | Harga')
    for i in range(len(monster_shop)):
        if i==len(monster_shop)-1:
            break
        spasi_type= len(' Type           ')-len(str(shop_m['type_m'][i]))-1
        spasi_atk= len(' ATK Power ')-len(str(shop_m['atk_m'][i]))-1
        spasi_def= len(' DEF Power ')-len(str(shop_m['def_m'][i]))-1
        spasi_hp= len(' HP   ')-len(str(shop_m['hp_m'][i]))-1
        spasi_stok= len(' Stok ')-len(str(shop_m['stok_m'][i]))-1

        print(f"{shop_m['id_m'][i]}  " + f"| {shop_m['type_m'][i]}" + spasi_type*" "  + f"| {shop_m['atk_m'][i]}" + spasi_atk*" " + f"| {shop_m['def_m'][i]}" + spasi_def*" " + f"| {shop_m['hp_m'][i]}" + spasi_hp*" " +  f"| {shop_m['stok_m'][i]}" + spasi_stok*" " + f"| {shop_m['harga_m'][i]}")

def lihat_potion(): 
    item_shop=parseran.read_csv('item_shop.csv')
    shop_p = buat_shop.load_data_p_shop_buat_shop_c()

    print('ID | Type                | Stok | Harga')
    for i in range(len(item_shop)):
        if i==len(item_shop)-1:
            break
        spasi_type_p= len(' Type                ')-len(str(shop_p['type_p'][i]))-1
        spasi_stok_p= len(' Stok ')-len(str(shop_p['stok_p'][i]))-1
        print(f"{shop_p['id_p'][i]}  | {shop_p['type_p'][i]}" +  spasi_type_p*" "  + f"| {shop_p['stok_p'][i]}" + spasi_stok_p*" " + f"| {shop_p['harga_p'][i]}")

def beli_monster(id_m:int):
    #mengecek kepemilikan monster
    monster_shop=parseran.read_csv('monster_shop.csv')
    monster_inventory =parseran.read_csv('monster_inventory.csv')
    user_login=parseran.read_csv('user_login.csv')
    data_oc=int(user_login[1][3])
    data_id=user_login[1][0]
    for i in range(len(monster_inventory)):
        if monster_inventory[i][1]==str(id_m) and monster_inventory[i][0]==data_id:
            print(f'Monster {monster[id_m][1]} sudah ada dalam inventory-mu! Pembelian dibatalkan.')
            return
    if data_oc < int(monster_shop[id_m][2]):
        print('OC-mu tidak cukup.')
        return
    if monster_shop[id_m][1]=='0':
        print('Stok Monster tersebut sudah habis!')
        return
    #mngurangi stok monster di monster_shop
    monster_shop[id_m][1]=str(int(monster_shop[id_m][1])-1)
    #mengurangi oc koin
    data_oc -= int(monster_shop[id_m][2])
    #menyimpan data di monster_inventory
    new_monster =[data_id,monster[id_m][0],'1']
    monster_inventory.append(new_monster)
    parseran.save_data('monster_inventory.csv',monster_inventory)
    parseran.save_data('monster_shop.csv',monster_shop)
    user_login[1][3]=str(data_oc)
    parseran.save_data('user_login.csv',user_login)
    print(f'Berhasil membeli item: {monster[id_m][1]}. Item sudah masuk ke inventory-mu')

def beli_potion(id_p:int, qty:int):
    item_inventory =parseran.read_csv('item_inventory.csv')
    item_shop =parseran.read_csv('item_shop.csv')
    user_login=parseran.read_csv('user_login.csv')
    data_oc=int(user_login[1][3])
    data_id=user_login[1][0]
    if data_oc < qty*int(item_shop[id_p][2]):
        print('OC-mu tidak cukup.')
        return
    if item_shop[id_p][1]=='0':
        print('Stok Potion tersebut sudah habis!')
        return
    if qty > int(item_shop[id_p][1]):
        print('Jumlah yang anda inginkan melebihi stok')
        return
    #cek potion dah ada atau belum, kalau ada stok tambah, klo gk ada buat line baru
    cek_punya=False
    for i in range(len(item_inventory)):
        if item_inventory[i][1]==item_shop[id_p][0] and item_inventory[i][0]==data_id:
            cek_punya=True
    if cek_punya:
        item_inventory[id_p][2]=str(int(item_inventory[id_p][2])+qty)
    else:
        new_potion=[data_id,item_shop[id_p][0],qty]
        item_inventory.append(new_potion)
        parseran.save_data('item_inventory.csv',item_inventory)
    #mngurangi stok potion di item_shop
    item_shop[id_p][1]=str(int(item_shop[id_p][1])-qty)
    #mengurangi oc koin
    data_oc -= qty*int(item_shop[id_p][2])
    parseran.save_data('item_shop.csv',item_shop)
    user_login[1][3]=str(data_oc)
    parseran.save_data('user_login.csv',user_login)
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
                qty = int(input('>>> Masukkan jumlah: '))
                beli_potion(id_pot,qty)
        pilihan=input('>>> Pilih aksi (lihat/beli/keluar): ')  
    print('Mr. Yanto bilang makasih, belanja lagi ya nanti :)')
"""
nanti kita ngurang2instok
validasi owca koin
nambahin data ke monster.csv

"""