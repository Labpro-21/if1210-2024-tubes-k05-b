import buat_shop
def bubble_sort_id_m(arr:list,dict:dict):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                dict["type_m"][j],dict["type_m"][j+1]=dict["type_m"][j+1],dict["type_m"][j]
                dict["atk_m"][j],dict["atk_m"][j+1]=dict["atk_m"][j+1],dict["atk_m"][j]
                dict["def_m"][j],dict["def_m"][j+1]=dict["def_m"][j+1],dict["def_m"][j]
                dict["hp_m"][j],dict["hp_m"][j+1]=dict["hp_m"][j+1],dict["hp_m"][j]
                dict["stok_m"][j],dict["stok_m"][j+1]=dict["stok_m"][j+1],dict["stok_m"][j]
                dict["harga_m"][j],dict["harga_m"][j+1]=dict["harga_m"][j+1],dict["harga_m"][j]
    return dict


def change_type_id(arr):
    for i in range(len(arr)):
        arr[i]=int(arr[i])
    return arr

def change_type_str(arr):
    for i in range(len(arr)):
        arr[i]=str(arr[i])
    return arr
def lihat_monster(monster_shop:list,monster:list):
    shop_m = buat_shop.load_data_m_shop_buat_shop_c(monster,monster_shop)
    change_type_id(shop_m["id_m"])
    bubble_sort_id_m(shop_m["id_m"],shop_m)
    change_type_str(shop_m["id_m"])
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

def lihat_potion(item_shop:list): 
    shop_p = buat_shop.load_data_p_shop_buat_shop_c(item_shop)

    print('ID | Type                | Stok | Harga')
    for i in range(len(item_shop)):
        if i==len(item_shop)-1:
            break
        spasi_type_p= len(' Type                ')-len(str(shop_p['type_p'][i]))-1
        spasi_stok_p= len(' Stok ')-len(str(shop_p['stok_p'][i]))-1
        print(f"{shop_p['id_p'][i]}  | {shop_p['type_p'][i]}" +  spasi_type_p*" "  + f"| {shop_p['stok_p'][i]}" + spasi_stok_p*" " + f"| {shop_p['harga_p'][i]}")

def beli_monster(id_m:int,monster_shop:list,monster_inventory:list,user_login:list,monster:list)->(list,list):
    #mengecek kepemilikan monster
    data_oc=int(user_login[1][3])
    data_id=user_login[1][0]
    for i in range(len(monster_inventory)):
        if monster_inventory[i][1]==str(id_m) and monster_inventory[i][0]==data_id:
            print(f'Monster {monster[id_m][1]} sudah ada dalam inventory-mu! Pembelian dibatalkan.')
            return (monster_inventory,user_login)
    if data_oc < int(monster_shop[id_m][2]):
        print('OC-mu tidak cukup.')
        return (monster_inventory,user_login)
    if monster_shop[id_m][1]=='0':
        print('Stok Monster tersebut sudah habis!')
        return (monster_inventory,user_login)
    #mngurangi stok monster di monster_shop
    monster_shop[id_m][1]=str(int(monster_shop[id_m][1])-1)
    #mengurangi oc koin
    data_oc -= int(monster_shop[id_m][2])
    #menyimpan data di monster_inventory
    new_monster =[data_id,monster[id_m][0],'1']
    monster_inventory.append(new_monster)
    user_login[1][3]=str(data_oc)
    print(user_login[1][3])
    print(f'Berhasil membeli item: {monster[id_m][1]}. Item sudah masuk ke inventory-mu')
    return (monster_inventory,user_login)

def beli_potion(id_p:int, qty:int,item_inventory:list,item_shop:list,user_login:list)->(list,list):
    data_oc=int(user_login[1][3])
    data_id=user_login[1][0]
    if data_oc < qty*int(item_shop[id_p][2]):
        print('OC-mu tidak cukup.')
        return (item_inventory,user_login)
    if item_shop[id_p][1]=='0':
        print('Stok Potion tersebut sudah habis!')
        return (item_inventory,user_login)
    if qty > int(item_shop[id_p][1]):
        print('Jumlah yang anda inginkan melebihi stok')
        return (item_inventory,user_login)
    #cek potion dah ada atau belum, kalau ada stok tambah, klo gk ada buat line baru
    cek_punya=False
    for i in range(len(item_inventory)):
        if item_inventory[i][1]==item_shop[id_p][0] and item_inventory[i][0]==data_id:
            cek_punya=True
            save_i=i
    if cek_punya:
        item_inventory[save_i][2]=str(int(item_inventory[save_i][2])+qty)
    else:
        print('s')
        new_potion=[data_id,item_shop[id_p][0],qty]
        item_inventory.append(new_potion)
    #mngurangi stok potion di item_shop
    item_shop[id_p][1]=str(int(item_shop[id_p][1])-qty)
    #mengurangi oc koin
    data_oc -= qty*int(item_shop[id_p][2])
    user_login[1][3]=str(data_oc)
    print(item_inventory)
    print(f'Berhasil membeli item: {qty} {item_shop[id_p][0]}. Item sudah masuk ke inventory-mu')
    return (item_inventory,user_login)

def shop_currency(monster_shop:list,item_shop:list,monster_inventory:list,item_inventory:list,user_login:list,monster:list):
    print('Irasshaimase! Selamat datang di SHOP!!')
    pilihan=input('>>> Pilih aksi (lihat/beli/keluar): ')    
    while pilihan!='keluar':
        if pilihan=='lihat':
            lihat_apa=input('>>> Mau lihat apa? (monster/potion): ')
            if lihat_apa=='monster':
                lihat_monster(monster_shop,monster)
            elif lihat_apa=='potion':
                lihat_potion(item_shop)
        elif pilihan=='beli':
            print(f'Umlah O.W.C.A koin mu: {user_login[1][3]}')
            beli_apa = input('>>> Mau beli apa? (monster/potion): ')
            if beli_apa=='monster':
                id_monst = int(input('>>> Masukkan id monster: '))
                (monster_inventory,user_login) = beli_monster(id_monst,monster_shop,monster_inventory,user_login,monster)
            elif beli_apa=='potion':
                id_pot = int(input('>>> Masukkan id potion: '))
                qty = int(input('>>> Masukkan jumlah: '))
                (item_inventory,user_login) =beli_potion(id_pot, qty,item_inventory,item_shop,user_login)
        pilihan=input('>>> Pilih aksi (lihat/beli/keluar): ')  
    print('Mr. Yanto bilang makasih, belanja lagi ya nanti :)')
"""
nanti kita ngurang2instok
validasi owca koin
nambahin data ke monster.csv

"""