def load_data_m(user_login:list,monster:list,monster_inv:list):
    data_id = user_login[1][0]
    data_m = {
        "id": [],
        "type": [],
        "lvl": [],
    }

    for i in range(len(monster_inv)):
        if monster_inv[i][0]==data_id:
            data_m["id"].append(monster_inv[i][1])
            data_m["lvl"].append(monster_inv[i][2])

            for m in monster:
                if m[0]==monster_inv[i][1]:
                    data_m["type"].append(m[1])
    return data_m
def lihat(data_m:dict):
    print('Selamat datang di Lab Dokter Asep !!!')
    print('============ MONSTER LIST ============')
    for i in range(len(data_m["id"])):
        print(f'{data_m["id"][i]}. {data_m["type"][i]} (Level: {data_m["lvl"][i]})')

    print('============ UPGRADE PRICE ============')
    print('1. Level 1 -> Level 2: 300 OC')
    print('2. Level 2 -> Level 3: 500 OC')
    print('3. Level 3 -> Level 4: 800 OC')
    print('4. Level 4 -> Level 5: 1000 OC')


def upgrade_m(lvl_now:int,pilih:int,data_m:list,monster_inv:list,user_login:list)->(list,list):
    harga = [300,500,800,1000]
    data_oc = user_login[1][3]
    data_id = user_login[1][0]
    if int(data_oc)<harga[lvl_now+1-2]:
        print('Maaf, koin anda tidak cukup')
        return (user_login,monster_inv)
    for i in range(len(monster_inv)):
        if monster_inv[i][0]==data_id and monster_inv[i][1]==data_m["id"][pilih-1]:
            monster_inv[i][2]=str(int(monster_inv[i][2])+1)
    data_oc = str(int(data_oc)-harga[lvl_now+1-2])
    print(f'Selamat, {data_m["type"][pilih-1]} berhasil diupgrade ke level {lvl_now+1}')
    user_login[1][3]=str(data_oc)
    return (user_login,monster_inv)

def laboratory(user_login:list,monster:list,monster_inventory:list):
    data_m=load_data_m(user_login,monster,monster_inventory)
    lihat(data_m)
    harga = [300,500,800,1000]
    pilih=input('>>> Pilih monster: ')
    while pilih!='keluar':
        i=int(pilih)-1
        if pilih in data_m["id"]:
            if int(data_m["lvl"][i])<5:
                lvl_now=int(data_m["lvl"][i])
                lvl_tlh_up = lvl_now+1
                print(f'{data_m["type"][i]} akan di-upgrade ke level {lvl_tlh_up}')
                print(f'Harga untuk melakukan upgrade {harga[lvl_tlh_up-2]}')
                yakin_up = input('>>> Lanjutkan upgrade (Y/N): ')
                if yakin_up=='Y':
                    (user_login,monster_inventory)=upgrade_m(lvl_now,i+1,data_m,monster_inventory,user_login)
                    data_m=load_data_m(user_login,monster,monster_inventory)
                    lvl_now=int(data_m["lvl"][i-1])
                    lvl_tlh_up = lvl_now+1
                else:
                    print(f'Woke, anda tidak jadi upgrade {data_m["type"][i-1]}')
            else:
                print('Maaf, monster yang Anda pilih sudah memiliki level maksimum')
        else:
            print('Monster Id Tidak ada di Inventory')
        pilih=input('>>> Pilih monster: ')