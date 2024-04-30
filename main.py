from commands import read_csv, trans_bahan, load, login, logout, summonjin, hapusjin, ubahjin, bangun, kumpul, batchkumpul, batchbangun, laporanjin, laporancandi, hancurkancandi, ayamberkokok, save, help, keluar
from Type import effective as eff
# MAIN PROGRAM
# F13
path=load()

# if load() success
users=eff(read_csv(path+"/user.csv")[0], read_csv(path+"/user.csv")[1])
candi=eff(read_csv(path+"/monster.csv")[0], read_csv(path+"/candi.csv")[1])
bahan_bangunan=trans_bahan(eff(read_csv(path+"/bahan_bangunan.csv")[0], read_csv(path+"/bahan_bangunan.csv")[1]))

(username, role, isLoggedIn)=('','',False)
while True:
    menu=input('>>> ')
    if menu=="LOGIN":
        #F01
        (username, role, isLoggedIn)=login(users, username, role)
    elif menu=='LOGOUT':
        #F02
        (username, role, isLoggedIn)=logout(username, role, isLoggedIn)
    elif menu =='SAVE':
         #
         save(users, candi, bahan_bangunan)
    elif menu=="HELP":
        # F15
        help(role)
    elif menu=='EXIT':
        # F16
        keluar(users, candi, bahan_bangunan)
    
