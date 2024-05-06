import argparse
import os
def read_csv(filename: str) -> list[list[any]]:
    values= []
    with open (filename, 'r') as file:
        for line in file:
            values.append(split(line))
    return values
def split(line: str) -> list[any]:
    out = []
    tmp = ''
    for c in line:
        if c == ';':
            out.append(tmp)
            tmp = ''
        else:
            if c != '\n':
                tmp += c
    out.append(tmp)
    return out
def change_type(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            try:
                data[i][j] = int(data[i][j])
            except:
                ValueError
            if data[i][j] == "True":
                data[i][j] = True
            elif data[i][j] == "False":
                data[i][j] = False
    return data
def loading():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_name",nargs='?', help="Input nama folder csv (required)")  
    args=parser.parse_args()

    # get the parameter
    folder_name=args.folder_name
    if folder_name==None:
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: python main.py <nama_folder>")
        exit()
    # Berpindah directory ke folder csv
    directory = parser.parse_args().folder_name
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
def load(folder):
    os.chdir('./' + str(folder))
    user = (read_csv("user.csv"))
    monster = (read_csv("monster.csv"))
    monster_shop = (read_csv("monster_shop.csv"))
    monster_inventory = (read_csv("monster_inventory.csv"))
    item_shop = (read_csv("item_shop.csv"))
    item_inventory = (read_csv("item_inventory.csv"))
    os.chdir('../')
    return user, monster, monster_shop, monster_inventory, item_shop, item_inventory
def convert_datas_to_string(data):
    data_string = ""
    for arr_data in data:
        arr_data_all_string = [str(var) for var in arr_data]
        data_string += ";".join(arr_data_all_string)
        data_string += "\n"
    return data_string
def save_data(file,data):
    data = convert_datas_to_string(data)
    f = open(file, "w") 
    f.write(data)
    f.close()
def save():
    parent = os.getcwd()
    checkDir = False
    
    while not checkDir:
        checkDir = True
        directory = input("Masukkan nama folder penyimpanan: ")
        for i in range(len(directory)):
            if directory[i] in ('/\:*?"><|'):
                checkDir = False
                print('nama folder anda mengandung /\:*?"><|')
                print()

    path = os.path.join(parent, directory)
    
    try:
        os.mkdir(path)
    except:
        FileExistsError
    os.chdir('./' + directory)
    print()
    print("Saving...")
    save_data("user.csv",user)
    save_data("monster.csv",monster)
    save_data("monster_shop.csv",monster_shop)
    save_data("monster_inventory.csv",monster_inventory)
    save_data("item_shop.csv",item_shop)
    save_data("item_inventory.csv",item_inventory)

    print("Data telah disimpan pada folder " + str(directory))
    os.chdir('../')
user  = []
monster = []
monster_shop = []
monster_inventory = []
item_inventory = []
item_shop = []
path = loading()

load(path)
print(path)
print(user)

