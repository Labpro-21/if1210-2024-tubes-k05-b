import parseran
monster_shop=parseran.read_csv('monster_shop.csv')
item_shop=parseran.read_csv('item_shop.csv')
monster =parseran.read_csv('monster.csv')
monster_inventory =parseran.read_csv('monster_inventory.csv')
item_inventory =parseran.read_csv('item_inventory.csv')

def load_data_m_shop_buat_shop_c()->dict:
    shop_m = {
        "id_m": [],
        "type_m": [],
        "atk_m": [],
        "def_m": [],
        "hp_m": [],
        "stok_m": [],
        "harga_m" : [],
    }
    monster =parseran.read_csv('monster.csv')
    monster_shop=parseran.read_csv('monster_shop.csv')
    for i in range(1,len(monster_shop)):
        shop_m['id_m'].append(monster_shop[i][0])
        shop_m['stok_m'].append(monster_shop[i][1])
        shop_m['harga_m'].append(monster_shop[i][2])

        for m in monster:
            if monster_shop[i][0]==m[0]:
                shop_m['type_m'].append(m[1])
                shop_m['atk_m'].append(m[2])
                shop_m['def_m'].append(m[3])
                shop_m['hp_m'].append(m[4])
    return shop_m

def load_data_p_shop_buat_shop_c()->dict:
    shop_p = {
        "id_p": [],
        "type_p": [],
        "stok_p": [],
        "harga_p": [],
    }
    item_shop=parseran.read_csv('item_shop.csv')
    for i in range(1,len(item_shop)):
        shop_p['id_p'].append(str(i))
        shop_p['type_p'].append(item_shop[i][0])
        shop_p['stok_p'].append(item_shop[i][1])
        shop_p['harga_p'].append(item_shop[i][2])
    return shop_p