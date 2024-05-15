import parseran
import Save

def save_oc_user_login(user:list,user_login:list):
    for u in user:
        if u[0]==user_login[1][0]:
            u[4]=user_login[1][3]
    parseran.save_data('user.csv',user)
    print('Data OC anda sudah tersimpan di database')

def Exit():
    user_login=parseran.read_csv('user_login.csv')
    user=parseran.read_csv('user.csv')
    konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while not ((konfirmasi == "y") or (konfirmasi == "Y") or (konfirmasi == "n") or (konfirmasi == "N")):
        konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if (konfirmasi == "y") or (konfirmasi == "Y"):
        save_oc_user_login(user,user_login)
        Save.new_save()
        exit()
    else:
        exit()