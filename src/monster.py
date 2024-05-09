from parseran import read_csv
from RNG import random_number
import math
monster_inv=read_csv('monster_inventory.csv')
monster=read_csv('monster.csv')
user_login=read_csv('user_login.csv')
data_id = user_login[1][0]
edit_att={
    "id": [],
    "type": [],
    "atk": [],
    "def": [],
    "hp": [],
    "lvl": [],
}

def edit_att_m():
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
    print(f'{defender[1]} terkena damage sebesar {hp_before-defender[4]}')
    return defender

def show_monster(player_monster:list,lvl:int):
    print(f"""Name      : {player_monster[1]}
ATK Power : {player_monster[2]}
DEF Power : {player_monster[3]}
HP        : {player_monster[4]}
Level     : {lvl}
""")
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