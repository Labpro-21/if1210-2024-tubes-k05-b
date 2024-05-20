import Save

def save_oc_user_login(user:list,user_login:list):
    for u in user:
        if u[0]==user_login[1][0]:
            u[4]=user_login[1][3]
    print('Data OC anda sudah tersimpan di database')
    return user

def Exit(user:list,user_login:list,monster:list,monster_shop:list,monster_inventory:list,item_inventory:list,item_shop:list):
    konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while not ((konfirmasi == "y") or (konfirmasi == "Y") or (konfirmasi == "n") or (konfirmasi == "N")):
        konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if (konfirmasi == "y") or (konfirmasi == "Y"):
        user = save_oc_user_login(user,user_login)
        Save.new_save(user,user_login,monster,monster_shop,monster_inventory,item_inventory,item_shop)
        print('Data csv sudah tersimpan')
    else:
        print('Data csv tidak tersimpan')