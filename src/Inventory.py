def inventory(user_login:list,monster:list,potion:list,monster_inventory:list):
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
    
    print(f'============ INVENTORY LIST (User ID: {user_login[1][0]}) ============')
    print(f'Jumlah O.W.C.A. Coin-mu sekarang {data_oc}')

    for x in range(len(potion)):
        inventory["user_id_inventory"].append(potion[x][0])
        inventory["type"].append(potion[x][1])
        inventory["quantity"].append(potion[x][2])

    for x in range(len(monster_inventory)):
        inventory["user_id_monster"].append(monster_inventory[x][0])
        inventory["monster_id"].append(monster_inventory[x][1])
        inventory["monster_level"].append(monster_inventory[x][2])

        # Count each occurrence of monster separately
        for m in monster:
            if str(monster_inventory[x][1]) == str(m[0]):
                inventory["monsters"].append(m[1])
                inventory["hp_monst"].append(m[4])
                inventory["atk_monst"].append(m[2])
                inventory["def_monst"].append(m[3])
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
    tampil=input('Ketikkan jenis item dan id untuk menampilkan detail item (monster/potion):\n>>> ')
    while tampil!="keluar":
        x=int(input(f'Pilih {tampil} urutan berapa:\n>>> '))
        if tampil=="monster":
            if x in save_id_m:
                print(f"{x}. Monster     {monst[x]} (Monster-ID: {monst_id[x+1]}, Level: {monst_lvl[x+1]}, Atk Power: {atk_monst[x]}, Def Power: {def_monst[x]}, HP: {hp_monst[x]}) ")
            else:
                print('Tidak ada data')
        elif tampil=="potion":
            if x in save_id_p:
                print(f"{x}. Potion      Type: {tipe_item[x]}, Quantity: {qty[x]}")
            else:
                print('Tidak ada data')
        tampil=input('Ketikkan jenis item dan id untuk menampilkan detail item (monster/potion):\n>>> ')