def logout(username:str, role:str, is_logged_in:bool) -> tuple[str,str,bool]:
    if (is_logged_in==True):
        is_logged_in = False
        username=""
        role=""
        print("Berhasil logout")
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")
    
    return (username, role, is_logged_in)