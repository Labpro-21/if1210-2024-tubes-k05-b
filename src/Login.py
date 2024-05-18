import parseran
import enkripsi
def save_data_login(id:str,username:str,role:str,oc:str,user_login:list):
    user_login[1][0]=id
    user_login[1][1]=username
    user_login[1][2]=role
    user_login[1][3]=oc
    user_login[1][4]='True'
    parseran.save_data('user_login.csv',user_login)

def login(user:list,user_login:list) :
    account_found = False
    if user_login[1][4] == "True":
        print(f'Anda telah login dengan username {user_login[1][1]}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.')
    else:
        username = input("Username : ") #meminta masukkan username
        password = input("Password : ") #meminta masukkan password
        # iterate over the rows in the user list
        #mengecek apakah akun tersebut ada atau tidak, jika tidak, login gagal
        for i in range(len(user)):
            # check if the username and password match
            if username == user[i][1]:
                if password == enkripsi.decode(user[i][2]):
                        account_found = True
                        data_username= username
                        data_role = user[i][3]
                        data_id = user[i][0]
                        data_oc = int(user[i][4])
                        save_data_login(data_id,data_username,data_role,data_oc,user_login)
                        print(f"Selamat datang, {data_role} {username}!")
                        print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
                        break
                else:
                    account_found = True
                    print("Password salah!")
                    break
            else :
                account_found = False

        if not account_found :
            print("Username tidak terdaftar")
