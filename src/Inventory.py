import data
from parseran import read_csv
def inventory():
    inventory = {
            "user_id_inventory": [],
            "type": [],
            "quantity": [],
            "user_id_monster": [],
            "monster_id": [],
            "monster_level": [],
            "monsters" : []
        }

    u_id_invent = inventory["user_id_inventory"]
    tipe_item = inventory["type"]
    qty = inventory["quantity"]
    u_id_monst = inventory["user_id_monster"]
    monst_id = inventory["monster_id"]
    monst_lvl = inventory["monster_level"]
    monst = inventory["monsters"]
    
    data.id=1
    monsters=read_csv('monster.csv')
    potion=read_csv('item_inventory.csv')
    monsters_inventory=read_csv('monster_inventory.csv')
    print(f'Jumlah O.W.C.A. Coin-mu sekarang {data.oc}')

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

    print("=====ITEMS=====")
    for x in range(1,len(potion)):
        print(f"{x}. Potion     User-ID: {u_id_invent[x]}, Type: {tipe_item[x]}, Quantity: {qty[x]}")
    print("====MONSTERS=====")
    for x in range(len(inventory['monsters'])):
        print(f"{x+1}. Monster    User-ID: {u_id_monst[x+1]}, {monst[x]} (Monster-ID: {monst_id[x+1]}, Level: {monst_lvl[x+1]})")

inventory()