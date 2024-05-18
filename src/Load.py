"""LOAD"""

import argparse
import os
import sys
import time
from parseran import read_csv_folder


def load():
    parser = argparse.ArgumentParser(description="Menjalankan main.py dalam folder yang spesifik di dalam folder parent 'data'")
    parser.add_argument("folder_name", nargs='?', help="Nama folder di dalam parent 'data'")
    args = parser.parse_args()

    if args.folder_name is None:
        print("Tidak ada nama folder yang diberikan!\nUsage : python main.py <folder_name>")
        sys.exit()

    folder_path = os.path.join(os.getcwd(),"data", args.folder_name)

    if os.path.exists(folder_path):
        #for i in range(4):
        #    print('Loading' + '.' * i, end='\r')
        #    time.sleep(0.5)
        #os.system('cls')
        user = read_csv_folder("user.csv",folder_path)
        user_login = read_csv_folder("user_login.csv",folder_path)
        monster = read_csv_folder("monster.csv",folder_path)
        monster_inventory = read_csv_folder("monster_inventory.csv",folder_path)
        monster_shop = read_csv_folder("monster_shop.csv",folder_path)
        item_inventory = read_csv_folder("item_inventory.csv",folder_path)
        item_shop = read_csv_folder("item_shop.csv",folder_path)
        return (True, user, user_login, monster, monster_inventory, monster_shop, item_inventory, item_shop)
    else:
        print(f"Folder '{args.nama_folder}' tidak ditemukan.")
        return (False, [], [], [], [], [], [], [])

