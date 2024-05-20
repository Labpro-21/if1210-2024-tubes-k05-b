import os
import time
import parseran
import Exit

def save(folder_name,user:list,user_login:list,monster:list,monster_shop:list,monster_inventory:list,item_shop:list,item_inventory:list):
    parseran.write_csv_to_folder(folder_name,'user',user)
    parseran.write_csv_to_folder(folder_name,'user_login',user_login)
    parseran.write_csv_to_folder(folder_name,'monster',monster)
    parseran.write_csv_to_folder(folder_name,'monster_shop',monster_shop)
    parseran.write_csv_to_folder(folder_name,'monster_inventory',monster_inventory)
    parseran.write_csv_to_folder(folder_name,'item_shop',item_shop)
    parseran.write_csv_to_folder(folder_name,'item_inventory',item_inventory)

def new_save(user:list,user_login:list,monster:list,monster_shop:list,monster_inventory:list,item_shop:list,item_inventory:list):
    folder_name = input("Masukkan nama folder: ")
    user = Exit.save_oc_user_login(user,user_login)
    if os.path.exists('./data'):
        if not os.path.exists(f'./data/{folder_name}'):
            print(f"Membuat folder data/{folder_name}...")
            os.mkdir(f'./data/{folder_name}')
            time.sleep(0.75)
    else:
        print("Membuat folder data...")
        time.sleep(0.75)
        os.mkdir('./data')
        print(f"Membuat folder data/{folder_name}...")
        time.sleep(1)
        os.mkdir(f'./data/{folder_name}')
        
    save(folder_name,user,user_login,monster,monster_shop,monster_inventory,item_shop,item_inventory)
    print(f"Berhasil menyimpan data di folder data/{folder_name}!")
