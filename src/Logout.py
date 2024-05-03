import data

def logout() :
    if data.login_status=="true":
        data.login_status = "false" #logout berarti login statusnya false
        print("Anda telah logout")
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout')
