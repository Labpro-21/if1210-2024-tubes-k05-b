import os
import time
import parseran

def save(folder_name):
    parseran.write_csv_to_folder(folder_name,'user')
    parseran.write_csv_to_folder(folder_name,'monster')
    parseran.write_csv_to_folder(folder_name,'monster_shop')
    parseran.write_csv_to_folder(folder_name,'monster_inventory')
    parseran.write_csv_to_folder(folder_name,'item_shop')
    parseran.write_csv_to_folder(folder_name,'item_inventory')

def new_save():
    folder_name = input("Masukkan nama folder: ")

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
        
    save(folder_name)
    print(f"Berhasil menyimpan data di folder data/{folder_name}!")
