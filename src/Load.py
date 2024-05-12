import argparse
import os
import parseran

def read_csv_files(folder):
    os.chdir(folder)
    user = parseran.read_csv("user.csv")
    monster = parseran.read_csv("monster.csv")
    monster_shop = parseran.read_csv("monster_shop.csv")
    monster_inventory = parseran.read_csv("monster_inventory.csv")
    item_shop = parseran.read_csv("item_shop.csv")
    item_inventory = parseran.read_csv("item_inventory.csv")
    os.chdir('../')
    return user, monster, monster_shop, monster_inventory, item_shop, item_inventory

def loading():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_name",nargs='?', help="Input nama folder csv (required)")  
    args = parser.parse_args()

    # get the parameter
    folder_name = args.folder_name
    if folder_name == None:
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: python main.py <nama_folder>")
        exit()
    # Berpindah directory ke folder csv
    directory = args.folder_name
    parent = os.getcwd()
    path = os.path.join(parent, directory)
    
    # Validasi folder ada
    if not os.path.exists(path):
        print("Nama folder yang diinputkan tidak ada")
    else:
        os.chdir('./' + directory)
        list_csv = ["user.csv","monster.csv","monster_shop.csv","monster_inventory.csv","item_shop.csv","item_inventory.csv"]
        for csv in list_csv:
            if not (os.path.exists(csv)):
                print(csv + " tidak ditemukan")
                return None
        os.chdir('../')
        return directory
