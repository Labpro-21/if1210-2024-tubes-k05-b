import parseran
def load_data_m_shop_buat_shop_c(monster:list,monster_shop:list)->dict:
    
    shop_data = {
        "id_m": [],
        "type_m": [],
        "atk_m": [],
        "def_m": [],
        "hp_m": [],
        "stok_m": [],
        "harga_m": []
    }
    #mengecek id di monster.csv dan monster.csv
    for ms in monster_shop:
        for m in monster:
            if ms[0] == m[0]:
                shop_data["id_m"].append(ms[0])
                shop_data["type_m"].append(m[1])
                shop_data["atk_m"].append(m[2])
                shop_data["def_m"].append(m[3])
                shop_data["hp_m"].append(m[4])
                shop_data["stok_m"].append(ms[1])
                shop_data["harga_m"].append(ms[2])
    return shop_data

def load_data_p_shop_buat_shop_c(item_shop:list)->dict:
    shop_p = {
        "id_p": [],
        "type_p": [],
        "stok_p": [],
        "harga_p": [],
    }
    for i in range(1,len(item_shop)):
        shop_p['id_p'].append(str(i))
        shop_p['type_p'].append(item_shop[i][0])
        shop_p['stok_p'].append(item_shop[i][1])
        shop_p['harga_p'].append(item_shop[i][2])
    return shop_p