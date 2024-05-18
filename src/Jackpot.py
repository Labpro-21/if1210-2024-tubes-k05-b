from RNG import random_number_arr,random_number
from parseran import read_csv,save_data

def check_id_m(monster:list,id_m:str,data_id:str)->bool:
    found=False
    for m in monster:
        if m[0]==id_m and m[1]==id_m:
            found=True
def jackpot(user_login:list,monster:list,monster_inventory:list) -> None:
    data_oc = int(user_login[1][3])
    data_id = user_login[1][0]
    print(data_oc)
    print("Apakah Anda siap untuk menguji keberuntungan? Menangkan Snorleks dengan 400 OC saja !!!")

    items = {
        0: ['Beras', 50],
        1: ['Telur', 100],
        2: ['Kopi', 200],
        3: ['Baju', 300],
        4: ['Koin', 400]
    }
    print("==== DAFTAR ITEM ====")
    print(f"1. Beras: 50 OC")
    print(f"2. Telur: 100 OC")
    print(f"3. Kopi: 200 OC")
    print(f"4. Baju: 300 OC")
    print(f"5. Koin: 500 OC")

    print("Mulai bermain? (y/n)")

    while True:
        mulai = input(">>> ").lower()
        if mulai =='y': 
            if data_oc >= 400:
                data_oc -= 400
                result=random_number_arr([0,5], 3)
                print(50*"=")
                print(17*"=" + f" {items[result[0]][0]} {items[result[1]][0]} {items[result[2]][0]} " + 17*"=")
                print(50*"=")

                if result[0] == result[1] and result[0] == result[2]:
                    random_id = random_number([0,len(monster)-1])
                    found = check_id_m(monster_inventory,str(random_id),data_id)
                    while found==True:
                        random_id = random_number([0,len(monster)-1])
                        found = check_id_m(monster_inventory,str(random_id),data_id)
                    monster_inventory.append([f'{data_id}',f'{random_id + 1}', '1'])
                    print(f"JACKPOT!!! Selamat, Anda mendapatkan monster {monster[random_id+ 1][1]}")
                else:
                    reward = items[result[0]][1] + items[result[1]][1] + items[result[2]][1]
                    data_oc += reward
                    user_login[1][3] = str(data_oc)
                    print(user_login[1][3])
                    print(f"Anda mendapatan {reward} OC, OC Anda sekarang {data_oc}.")
            else:
                print(f"Anda tidak memiliki cukup OC, OC anda hanya {data_oc}.")
            break
        elif mulai=='n':
            print("Terima kasih sudah mengunjungi Jackpot")
            break
        else:
            print("Input tidak valid")
#jackpot()