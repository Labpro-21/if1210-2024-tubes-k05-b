from parseran import read_csv
def inventory():
    user_login=read_csv('user_login.csv')
    data_oc=user_login[1][3]
    inventory = {
            "user_id_inventory": [],
            "type": [],
            "quantity": [],
            "user_id_monster": [],
            "monster_id": [],
            "monster_level": [],
            "monsters" : [],
            "hp_monst" : [],
            "atk_monst" : [],
            "def_monst" : [],
        }

    u_id_invent = inventory["user_id_inventory"]
    tipe_item = inventory["type"]
    qty = inventory["quantity"]
    u_id_monst = inventory["user_id_monster"]
    monst_id = inventory["monster_id"]
    monst_lvl = inventory["monster_level"]
    monst = inventory["monsters"]
    hp_monst = inventory["hp_monst"]
    atk_monst = inventory["atk_monst"]
    def_monst = inventory["def_monst"]
    
    monsters=read_csv('monster.csv')
    potion=read_csv('item_inventory.csv')
    monsters_inventory=read_csv('monster_inventory.csv')
    print(f'============ INVENTORY LIST (User ID: {user_login[1][0]}) ============')
    print(f'Jumlah O.W.C.A. Coin-mu sekarang {data_oc}')

    for x in range(len(potion)):
        inventory["user_id_inventory"].append(potion[x][0])
        inventory["type"].append(potion[x][1])
        inventory["quantity"].append(potion[x][2])

    for x in range(len(monsters_inventory)):
        inventory["user_id_monster"].append(monsters_inventory[x][0])
        inventory["monster_id"].append(monsters_inventory[x][1])
        inventory["monster_level"].append(monsters_inventory[x][2])

        # Count each occurrence of monster separately
        for monster in monsters:
            if str(monsters_inventory[x][1]) == str(monster[0]):
                inventory["monsters"].append(monster[1])
                inventory["hp_monst"].append(monster[4])
                inventory["atk_monst"].append(monster[2])
                inventory["def_monst"].append(monster[3])
    print("================ITEMS=================")
    save_id_p=[]
    for x in range(1,len(potion)):
        if u_id_invent[x]==user_login[1][0]:
            print(f"{x}. Potion      (Type: {tipe_item[x]}, Quantity: {qty[x]})")
            save_id_p.append(x)
    print("===============MONSTERS===============")
    save_id_m=[]
    for x in range(len(inventory["monsters"])):
        if u_id_monst[x+1]==user_login[1][0]:
            print(f"{x}. Monster    {monst[x]} (Monster-ID: {monst_id[x+1]}, Level: {monst_lvl[x+1]}, HP: {hp_monst[x]}) ")
            save_id_m.append(x)
    print('m: monster, p:potion')

    id_tampil=input('Ketikkan jenis item dan id untuk menampilkan detail item (m{urutan}/p{urutan}):\n>>> ')
    while id_tampil!="keluar":
        x=int(id_tampil[1])
        if id_tampil[0]=="m":
            if x in save_id_m:
                print(f"{x}. Monster     {monst[x]} (Monster-ID: {monst_id[x+1]}, Level: {monst_lvl[x+1]}, Atk Power: {atk_monst[x]}, Def Power: {def_monst[x]}, HP: {hp_monst[x]}) ")
            else:
                print('Tidak ada data')
        elif id_tampil[0]=="p":
            if x in save_id_p:
                print(f"{x}. Potion      Type: {tipe_item[x]}, Quantity: {qty[x]}")
            else:
                print('Tidak ada data')
        id_tampil=input('Ketikkan jenis item dan id untuk menampilkan detail item (m{urutan}/p{urutan}):\n>>> ')