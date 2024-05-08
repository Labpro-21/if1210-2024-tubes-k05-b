from loadnsave import save
from parseran import save_data,read_csv
user_login=read_csv('user_login.csv')
user=read_csv('user.csv')
def save_oc_user_login(user:list,user_login:list):
    for u in user:
        if u[0]==user_login[1][0]:
            u[4]=user_login[1][3]
    save_data('user.csv',user)
    print('Data OC anda sudah tersimpan di database')

def exit():
    konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    while not ((konfirmasi == "y") or (konfirmasi == "Y") or (konfirmasi == "n") or (konfirmasi == "N")):
        konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if (konfirmasi == "y") or (konfirmasi == "Y"):
        save_oc_user_login(user,user_login)
        save()
        exit()
    else:
        exit()