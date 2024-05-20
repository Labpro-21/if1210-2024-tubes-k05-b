import time
import Monster_edt
import Potion
import RNG
import parseran
import colorizer as clr
import os
from Help import Help

def kurangi_qty(data_id: str, type_p: str,item_inv:list)->list:
    for p in item_inv:
        if p[0] == data_id and p[1] == type_p:
            p[2] = str(int(p[2]) - 1)
    return item_inv

def fight(monster_lvl:int,r_monster:list,user_login:list,item_inv:list,monster_inv:list,monster:list):
    data_username = user_login[1][1]
    data_id = user_login[1][0]
    stat = {
        'win': True,
        'total_damage': 0,
        'damage_taken': 0,
    }
    r_monster = Monster_edt.edit_att_r_m(r_monster, monster_lvl)
    print(f'RAWRR, Monster {r_monster[1]} telah muncul !!!\n')
    Monster_edt.monster_art_musuh()

    print(12 * "=" + "MONSTER LIST" + 12 * "=" + '\n')

    user_monster = Monster_edt.edit_att_m(monster_inv,monster,user_login)
    for idx in range(len(user_monster["type"])):
        print(f'{idx+1}. {user_monster["type"][idx]}')
    
    pilih = int(input("\nPilih monster untuk bertarung (angka): "))
    while not (1 <= pilih <= len(user_monster["id"])):
        print(clr.colored("Pilihan nomor tidak tersedia!", 'red'))
        pilih = int(input("Pilih monster untuk bertarung (angka): "))
    
    player_monster = []
    player_monster.append(user_monster["id"][pilih - 1])
    player_monster.append(user_monster["type"][pilih - 1])
    player_monster.append(user_monster["atk"][pilih - 1])
    player_monster.append(user_monster["def"][pilih - 1])
    player_monster.append(user_monster["hp"][pilih - 1])
    player_monster.append(user_monster["lvl"][pilih - 1])
    base_hp = user_monster["hp"][pilih - 1]
    
    time.sleep(1)
    
    Monster_edt.monster_art_user()
    print(f"Agent {data_username} mengeluarkan monster {player_monster[1]} !!!\n")
    Monster_edt.show_monster(player_monster, player_monster[5])
    time.sleep(2)
    

    current_potion = {
        'strength': False,
        'resilience': False,
        'healing': False
    }

    turn = 1
    while True:
        time.sleep(0.75)
        if r_monster[4] == 0:
            return stat
        elif player_monster[4] == 0:
            stat['win'] = False
            return stat

        if turn % 2 == 1:
            print("\n" + 12 * "=" + clr.colored(f"TURN {turn} ({player_monster[1]})", 'magenta') + 12 * "=")
            print('1. Attack\n2. Use Potion\n3. Quit')
            choice = int(input("Pilih perintah (angka): "))
            while choice < 1 or choice > 3:
                print("Pilihan tidak ditemukan.")
                choice = int(input("Pilih perintah (angka): "))
            
            if choice == 1:
                print(f"SCHWINKKK, {player_monster[1]} menyerang {r_monster[1]}(musuh) !!!\n")
                hp_awal = r_monster[4]
                time.sleep(1)
                
                r_monster = Monster_edt.atk(player_monster, r_monster)
                Monster_edt.show_monster(r_monster, monster_lvl)
                stat["total_damage"] += hp_awal - r_monster[4]
            elif choice == 2:
                user_potion = Potion.load_data_p(item_inv,user_login)
                if user_potion == []:
                    print("Kamu tidak memiliki potion. Beli potion di shop.")
                else:
                    while True:
                        idx = 0
                        for p in user_potion:
                            if p[0] == 'strength':
                                print(f'{idx+1}. Strength Potion (Qty: {p[1]}) - Increase ATK Power')
                            elif p[0] == 'resilience':
                                print(f"{idx+1}. Resilience Potion (Qty: {p[1]}) - Increase DEF Power")
                            elif p[0] == 'healing':
                                print(f"{idx+1}. Healing Potion (Qty: {p[1]}) - Restores Health")
                            idx += 1
                        print(f'{idx+1}. Cancel')
                        pilih_p = int(input("\nPilih Potion (angka): "))
                        if pilih_p == idx + 1:
                            print('tes')
                            break
                        elif not (1 <= pilih_p <= idx):
                            print('Potion tidak ditemukan')
                            break
                        elif int(user_potion[pilih_p - 1][1]) == 0:
                            print("Potion kamu sudah habis")
                            break
                        
                        potion_name = user_potion[pilih_p - 1][0]
                        if current_potion[potion_name]:
                            print(f"Kamu mencoba memberikan ramuan ini kepada {player_monster[1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                            break

                        if potion_name == 'strength':
                            player_monster[2] *= 1.05
                            print(f"Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi {player_monster[1]} dan gerakannya menjadi lebih cepat dan mematikan")
                        elif potion_name == 'resilience':
                            if player_monster[3] * 1.05 <= 50:
                                player_monster[3] *= 1.05
                            else:
                                player_monster[3] = 50
                            print(f"Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {player_monster[1]} yang membuatnya terlihat semakin tangguh dan sulit dilukai")
                        elif potion_name == 'healing':
                            player_monster[4] += 0.25 * base_hp
                            if player_monster[4] > base_hp:
                                player_monster[4] = base_hp
                            print(f"Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh {player_monster[1]} sembuh dengan cepat. Dalam sekejap, {player_monster[1]} terlihat kembali prima dan siap melanjutkan pertempuran") 

                        current_potion[potion_name] = True
                        item_inv = kurangi_qty(data_id, potion_name, item_inv)
                        break
            elif choice == 3:
                print("Berhasil kabur!")
                stat['win'] = False
                return stat
            
            turn += 1
            time.sleep(3.25)
            
        else:
            print("\n" + 12 * "=" + clr.colored(f"TURN {turn} ({r_monster[1]} (musuh))", "blue") + 12 * "=")
            print(f"SCHWINKKK, {r_monster[1]} (musuh) menyerang {player_monster[1]} !!!")
            hp_awal = player_monster[4]
            time.sleep(1)
            
            player_monster = Monster_edt.atk(r_monster, player_monster)
            Monster_edt.show_monster(player_monster, player_monster[5])

            stat['damage_taken'] += hp_awal - player_monster[4]
            turn += 1
            time.sleep(3.25)
            
            

def battle(user_login:list,monster:list,item_inv:list,monster_inv:list)->list:
    id_monster = RNG.random_number([1, len(monster)])
    monster_lvl = RNG.random_number([1, 5])
    random_monster = []
    for m in monster:
        if m[0] == str(id_monster):
            random_monster.append(m[0])
            random_monster.append(m[1])
            random_monster.append(int(m[2]))
            random_monster.append(int(m[3]))
            random_monster.append(int(m[4]))
    random_monster.append(monster_lvl)
    result = fight(monster_lvl, random_monster,user_login,item_inv,monster_inv,monster)
    if result['win']:
        reward = RNG.random_number([5, 30])
        user_login[1][3] = str(int(user_login[1][3]) + reward)
        print(clr.colored(f"Selamat, Anda berhasil mengalahkan monster {random_monster[1]}. Anda mendapatkan {reward} OC.", 'yellow'))
    else:
        print(clr.colored(f"Yahhh, Anda dikalahkan monster {random_monster[1]}. Jangan menyerah, coba lagi !!!", 'grey'))
    return user_login
# battle()