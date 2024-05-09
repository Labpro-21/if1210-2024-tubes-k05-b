import time, copy
from colorama import Fore, Back, Style
from . import Database, Function, RNG, Inventory, Help, Battle


def displayArenaStat(stat):
    print(25*"=" + "STAT" + 25*"=")
    print(f"""
Jumlah Hadiah           : {stat['oc']}
Jumlah Stage            : {stat['stage']}
Total Damage Diberikan  : {stat['totalDamage']}
Total Damage Diterima   : {stat['damageTaken']}
""")


def Arena():
    if not Database.isLogin:
        Help.displayHelp()

    else:
        multiplier = 7
        addingConstant = 0
        totalMonster = len(Database.monster_art)
        totalLevel = 5
        allMonster = RNG.lcg(multiplier, addingConstant, totalMonster, totalLevel)

        stat = {
            'totalDamage' : 0,
            'damageTaken' : 0,
            'oc' : 0,
            'stage' : 0
        }

        for i in range(totalLevel):
            monster = copy.copy(Database.monster[allMonster[i]])
            monsterLevel = i + 1
            monster = Function.updateAttribute(monster, monsterLevel)
            
            result = Battle.fight(monsterLevel, monster)
            stat['damageTaken'] += result['damageTaken']
            stat['totalDamage'] += result['totalDamage']

            if result['win']:
                reward = int(30 * ((1 + i) ** 1.1))

                Database.oc += reward
                Database.user[Database.id - 1][4] = str(Database.oc)
                stat['stage'] += 1
                stat['oc'] += reward
                print(f"Selamat, Anda berhasil mengalahkan monster {monster[1]}. \nSTAGE CLEARED! Anda mendapatkan {reward} OC pada stage ini.")
                time.sleep(1)
                print("Memulai stage berikutnya...")
                time.sleep(1)
            else:
                print(f"Yahhh, Anda dikalahkan monster {monster[1]}. Jangan menyerah, coba lagi !!!")
                break

        if stat['stage'] == 5:
            print("Selamat, Anda berhasil menyelesaikan seluruh stage!")


        displayArenaStat(stat)