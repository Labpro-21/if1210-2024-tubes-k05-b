from parseran import read_csv,save_data
import data

monster=read_csv('monster.csv')
monster_inv=read_csv('monster_inventory.csv')
data_m = {
    "id": [],
    "type": [],
    "lvl": [],
}

harga = [300,500,800,1000]
for i in range(len(monster_inv)):
    if monster_inv[i][0]==data.id:
        data_m["id"].append(monster_inv[i][1])
        data_m["lvl"].append(monster_inv[i][2])

        for m in monster:
            if m[0]==monster_inv[i][1]:
                data_m["type"].append(m[1])
def lihat():
    print('Selamat datang di Lab Dokter Asep !!!')
    print('============ MONSTER LIST ============')
    for i in range(len(data_m["id"])):
        print(f'{data_m["id"][i]}. {data_m["type"][i]} (Level: {data_m["lvl"][i]})')

    print('============ UPGRADE PRICE ============')
    print('1. Level 1 -> Level 2: 300 OC')
    print('2. Level 2 -> Level 3: 500 OC')
    print('3. Level 3 -> Level 4: 800 OC')
    print('4. Level 4 -> Level 5: 1000 OC')


def upgrade_m(lvl_now:int,pilih:int):
    if data.oc<harga[lvl_now+1-2]:
        print('Maaf, koin anda tidak cukup')
        return
    for i in range(len(monster_inv)):
        if monster_inv[i][0]==data.id and monster_inv[i][1]==data_m["id"][pilih-1]:
            monster_inv[i][2]=str(int(monster_inv[i][2])+1)
    data.oc-=harga[lvl_now+1-2]
    print(f'Selamat, {data_m["type"][pilih-1]} berhasil diupgrade ke level {lvl_now+1}')
    save_data('monster_inventory.csv',monster_inv)

def lab():
    lihat()
    pilih=input('>>> Pilih monster: ')
    while pilih!='keluar':
        i=int(pilih)
        if int(data_m["lvl"][i+1])<5:
            lvl_now=int(data_m["lvl"][i-1])
            lvl_tlh_up = lvl_now+1
            print(f'{data_m["type"][i-1]} akan di-upgrade ke level {lvl_tlh_up}')
            print(f'Harga untuk melakukan upgrade {harga[lvl_tlh_up-2]}')
            yakin_up = input('>>> Lanjutkan upgrade (Y/N): ')
            if yakin_up=='Y':
                upgrade_m(lvl_now,i)
            else:
                print(f'Woke, anda tidak jadi upgrade {data_m["type"][i-1]}')
        else:
            print('Maaf, monster yang Anda pilih sudah memiliki level maksimum')
        pilih=input('>>> Pilih monster: ')
lab()
    

