from RNG import random_number
from Help import help
from Battle import fight
from monster import edit_att_r_m
from parseran import read_csv,save_data
import time
def show_arena_stat(stat:dict):
    print(25*"=" + "STAT" + 25*"=")
    print(f"""
Jumlah Hadiah           : {stat['oc']}
Jumlah Stage            : {stat['stage']}
Total Damage Diberikan  : {stat['total_damage']}
Total Damage Diterima   : {stat['damage_taken']}
""")

def arena():
    user_login = read_csv("user_login.csv")
    status_login=user_login[1][4]
    data_monster = read_csv("monster.csv")
    if status_login=="False":
        help()
    else:
        id_monster = []
        if len(data_monster)>5:
            while len(id_monster) < 5:
                random_id = str(random_number([1, len(data_monster)]))
                if random_id not in id_monster:
                    id_monster.append(random_id)
        else:
            while len(id_monster) < 5:
                random_id = str(random_number([1, len(data_monster)]))
                if random_id not in id_monster:
                    id_monster.append(random_id)
                if len(id_monster) >= len(data_monster):
                    id_monster.append(random_id)
        print(id_monster)
        stat = {
            'total_damage' : 0,
            'damage_taken' : 0,
            'oc' : 0,
            'stage' : 0,
        }
        for i in range(5):
            for m in data_monster:
                if m[0]==str(id_monster[i]):
                    monster = m
                    monster_level=i+1
                    print(monster)
                    monster = edit_att_r_m(monster,monster_level)
                    result = fight(monster_level,monster)
                    stat['damage_taken'] += result['damage_taken']
                    stat['total_damage'] += result['total_damage']

            if result['win']:
                reward = int(30 * (i + 1)**1.25)

                user_login[1][3] = str(int(user_login[1][3])+reward)
                stat["stage"] += 1
                stat["oc"] += reward
                print(f"Selamat, Anda berhasil mengalahkan monster {monster[1]}. \nSTAGE CLEARED! Anda mendapatkan {reward} OC pada stage ini.")
                time.sleep(0.75)
                if not(stat['stage'] == 5):
                    print("Memulai stage berikutnya...")
                save_data('user_login.csv',user_login)
            else:
                print(f"Yahhh, Anda dikalahkan monster {monster[1]}. Jangan menyerah, coba lagi !!!")
                break
        
        if stat['stage'] == 5:
            print("Selamat, Anda berhasil menyelesaikan seluruh stage!")
        
        show_arena_stat(stat)
arena()


