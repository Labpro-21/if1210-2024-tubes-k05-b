from RNG import random_number
import math
import colorizer as clr

def edit_att_m(monster_inv:list,monster:list,user_login:list)->dict:
    data_id = user_login[1][0]
    edit_att = {
        "id": [],
        "type": [],
        "atk": [],
        "def": [],
        "hp": [],
        "lvl": [],
    }
    for m in monster_inv:
        if m[0]==data_id and m[1] not in edit_att["id"]:
            edit_att["id"].append(m[1])
            edit_att["lvl"].append(int(m[2]))
            lvl=int(m[2])
            for mo in monster:
                if mo[0]==m[1]:
                    edit_att["type"].append(mo[1])
                    edit_att["atk"].append(monst_att(lvl,mo[2]))
                    if monst_att(lvl,mo[3])<=50:
                        edit_att["def"].append(monst_att(lvl,mo[3]))
                    else:
                        edit_att["def"].append(50)
                    edit_att["hp"].append(monst_att(lvl,mo[4]))
    return edit_att

def atk(attacker:list , defender:list) -> list:
    rng_atk = random_number([-30,30])
    atk_power = attacker[2]*(100+rng_atk)/100
    def_power = random_number([0,defender[3]])
    total_minus = atk_power*(100-def_power)/100
    hp_before = defender[4]
    if math.floor(defender[4]-total_minus)>0:
        defender[4] = math.floor(defender[4]-total_minus)
    else:
        defender[4]=0
    print(clr.colored(f"{defender[1]}", 'red') + ' terkena damage sebesar ' + clr.colored(f"{hp_before-defender[4]}", 'red'))
    return defender

def show_monster(player_monster:list,lvl:int):
    print(f"Name      : " + clr.colored(f"{player_monster[1]}", 'red'))
    print(f"ATK Power : " + clr.colored(f"{player_monster[2]}", 'red'))
    print(f"DEF Power : " + clr.colored(f"{player_monster[3]}", 'red'))
    print(f"HP        : " + clr.colored(f"{player_monster[4]}", 'red'))
    print(f"Level     : " + clr.colored(f"{lvl}", 'red'))
    return
def edit_att_r_m(monster:list,level:int)->list:
    monster[2]=monst_att(level,monster[2])
    monster[3]=monst_att(level,monster[3])
    if monster[3]>50:
        monster[3]=50
    monster[4]=monst_att(level,monster[4])
    return monster
def monst_att(level:int,nilai:str)->int:
    return int(float(nilai) * (1 + (level - 1)/10))

def monster_art_user():
    print("""
          /\----/\_   
         /         \   /|
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \  |   |   |
         |  |   |   |
          \._\   \._\ 

    """)

def monster_art_musuh():
    print("""
           _/\----/\.
          /         \     /\.
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |      
         /  |     |   \  |  |      
        /   `^^^^^'    \ |  |      
      ./  /|            \|  |_     
     /   / |         |\__     /    
     \  /  |         |   |__|      
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__  
    """)