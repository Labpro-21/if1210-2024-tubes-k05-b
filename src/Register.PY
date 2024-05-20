
import os
import parseran
import enkripsi

# Fungsi untuk melakukan registrasi
def register(users:list, monsters:list,monster_inventory:list,user_login:list)->(list,list):
    if user_login[1][4]=="True":
        print(f"Register gagal! Anda telah login dengan username {user_login[1][1]} silahkan lakukan 'LOGOUT' sebelum melakukan register.")
        return (users,monster_inventory)
    else:
        # Memasukkan input username dan password
        username = input("Masukan username: ")
        password = input("Masukan password: ")

        # Validasi username
        if not all(char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-0123456789" for char in username):
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            return (users,monster_inventory)
        # Cek apakah username telah terpakai atau sudah login dengan akun yang baru diregiste
        for i in range(len(users)):
            if users[i][1] == username:
                print("Username", username, "sudah terpakai, silahkan gunakan username lain!")
                return (users,monster_inventory)
    print("Silahkan pilih salah satu monster sebagai monster awalmu.")

    for i in range(1,len(monsters)):
        print(f'   {i}. {monsters[i][1]}')

    # Pemilihan monster
    monster_choice = int(input("Monster pilihanmu:\n"))
    while monster_choice < 1 or monster_choice > len(monsters):
        print("Pilihan monster tidak valid!")
        monster_choice = int(input("Monster pilihanmu:\n"))
    
    # Proses registrasi
    new_agent_id = len(users) if users else 1
    new_agent = [str(new_agent_id), username, enkripsi.encode(password), 'Agent', 0]
    users.append(new_agent)

    data_role = users[new_agent_id][3]
    data_username= username
    data_id = str(new_agent_id)
    data_oc = '0'
    for_monster_inventory = [str(new_agent_id),str(monster_choice),'1']
    monster_inventory.append(for_monster_inventory)
    print("Selamat datang Agent", username + ". Mari kita mengalahkan Dr. Asep Spakbor dengan", monsters[monster_choice][1] + "!. silahkan tekan login!")
    return (users,monster_inventory)