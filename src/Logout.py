import data

def logout() :
    if data.login_status=="true":
        data.login_status = "false" #logout berarti login statusnya false
        data.id=0
        data.username = "null"
        data.role = "null"
        data.oc=0
        print("Anda telah logout")
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout')