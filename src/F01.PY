import csv
import os

def load_monsters(filename):
    monsters = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            monsters.append({
                'id': int(row['id']),
                'type': row['type'],
                'atk_power': int(row['atk_power']),
                'def_power': int(row['def_power']),
                'hp': int(row['hp'])
            })
    return monsters

def load_agents(filename):
    agents = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            agents.append({
                'id': int(row['id']),
                'username': row['username'],
                'password': row['password'],
                'role': row['role'],
                'oc': int(row['oc'])
            })
    return agents

def save_agents(filename, agents):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['id', 'username', 'password', 'role', 'oc']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for agent in agents:
            writer.writerow({
                'id': agent['id'],
                'username': agent['username'],
                'password': agent['password'],
                'role': agent['role'],
                'oc': agent['oc']
            })

def register():
    # Fungsi untuk melakukan registrasi
    def register_user(agents, monsters):
        # Memasukkan input username dan password
        username = input("Masukan username: ")
        password = input("Masukan password: ")

        # Mendapatkan direktori home pengguna
        home_dir = os.path.expanduser("~")

        # Path ke file user.csv dan monster.csv
        user_csv_path = os.path.join(home_dir, 'Documents', '1. FILE ITB', 'TUBES DASPRO', 'if1210-2024-tubes-k05-b', 'data', 'user.csv')
        monster_csv_path = os.path.join(home_dir, 'Documents', '1. FILE ITB', 'TUBES DASPRO', 'if1210-2024-tubes-k05-b', 'data', 'monster.csv')

        # Memuat agen
        agents = load_agents(user_csv_path)
        monsters = load_monsters(monster_csv_path)

        # Validasi username
        if not username.replace('_', '').replace('-', '').isalnum():
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            return

        # Cek apakah username telah terpakai atau sudah login dengan akun yang baru diregister
        for agent in agents:
            if agent['username'] == username:
                if agent['password'] == password:
                    print("Register gagal! Anda telah login dengan username", username + ", silahkan lakukan 'LOGOUT' sebelum melakukan register.")
                    return
                else:
                    print("Username", username, "sudah terpakai, silahkan gunakan username lain!")
                    return

        # Pemilihan monster
        monster_choice = int(input("Silahkan pilih salah satu monster sebagai monster awalmu:\n"))
        if monster_choice < 1 or monster_choice > len(monsters):
            print("Pilihan monster tidak valid!")
            return

        # Proses registrasi
        new_agent_id = max([agent['id'] for agent in agents], default=0) + 1
        new_agent = {
            'id': new_agent_id,
            'username': username,
            'password': password,
            'role': 'agent',
            'oc': 0,
            'monster': monsters[monster_choice - 1]
        }
        agents.append(new_agent)
        print("Selamat datang Agent", username + ". Mari kita mengalahkan Dr. Asep Spakbor dengan", new_agent['monster']['type'] + "!")
        save_agents('user.csv', agents)

    # Memanggil fungsi register_user
    agents = []
    monsters = []
    register_user(agents, monsters)

# Memanggil fungsi register
register()

"""
1;bangkitganteng;inipassword124;agent;0
2;Purry;inipassword124;agent;0
"""