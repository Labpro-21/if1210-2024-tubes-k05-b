import RNG
import Help
import Battle
import parseran
import time
import Monster_edt
def show_arena_stat(stat:dict):
    print(25*"=" + "STAT" + 25*"=")
    print(f"""
Jumlah Hadiah           : {stat['oc']}
Jumlah Stage            : {stat['stage']}
Total Damage Diberikan  : {stat['total_damage']}
Total Damage Diterima   : {stat['damage_taken']}
""")

def arena(user_login:list,data_monster:list,item_inv:list,monster_inv:list)->list:
    id_monster = RNG.random_number_arr([1,len(data_monster)],5)
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
                monster = Monster_edt.edit_att_r_m(monster,monster_level)
                result = Battle.fight(monster_level,monster,user_login,item_inv,monster_inv,data_monster)
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
        else:
            print(f"Yahhh, Anda dikalahkan monster {monster[1]}. Jangan menyerah, coba lagi !!!")
            break
    
    if stat['stage'] == 5:
        print("Selamat, Anda berhasil menyelesaikan seluruh stage!")
    
    show_arena_stat(stat)
    return user_login
#arena()