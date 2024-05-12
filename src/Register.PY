
import os
import parseran
import enkripsi
import Login
def register():
    # Fungsi untuk melakukan registrasi
    def register_user(users, monsters):
        user_login=parseran.read_csv('user_login.csv') 
        if user_login[1][4]=="True":
            print(f"Register gagal! Anda telah login dengan username {user_login[1][1]} silahkan lakukan 'LOGOUT' sebelum melakukan register.")
            return
        else:
            # Memasukkan input username dan password
            username = input("Masukan username: ")
            password = input("Masukan password: ")

            # Memuat agen
            users = parseran.read_csv('user.csv')
            monsters = parseran.read_csv('monster.csv')
            monster_inventory = parseran.read_csv('monster_inventory.csv')
            # Validasi username
            if not all(char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-0123456789" for char in username):
                print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
                return
            # Cek apakah username telah terpakai atau sudah login dengan akun yang baru diregiste
            for i in range(len(users)):
                if users[i][1] == username:
                    print("Username", username, "sudah terpakai, silahkan gunakan username lain!")
                    return
        print("Silahkan pilih salah satu monster sebagai monster awalmu.")
        print(monsters)
        for i in range(1,len(monsters)):
            print(f'{i}. {monsters[i][1]}')

        # Pemilihan monster
        monster_choice = int(input("Silahkan pilih salah satu monster sebagai monster awalmu:\n"))
        if monster_choice < 1 or monster_choice > len(monsters):
            print("Pilihan monster tidak valid!")
            return
        
        # Proses registrasi
        new_agent_id = len(users) if users else 1
        new_agent = [new_agent_id, username, enkripsi.encode(password), 'Agent', 0]
        users.append(new_agent)

        data_role = users[new_agent_id][3]
        data_username= username
        data_id = str(new_agent_id)
        data_oc = '0'
        for_monster_inventory = [new_agent_id,monster_choice,1]
        monster_inventory.append(for_monster_inventory)
        print("Selamat datang Agent", username + ". Mari kita mengalahkan Dr. Asep Spakbor dengan", monsters[monster_choice][1] + "!")
        Login.save_data_login(data_id,data_username,data_role,data_oc)
        parseran.save_data('user.csv', users)
        parseran.save_data('monster_inventory.csv', monster_inventory)
    users = []
    monsters = parseran.read_csv('monster.csv')
    register_user(users, monsters)