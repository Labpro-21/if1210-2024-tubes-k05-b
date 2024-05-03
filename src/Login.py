import data
from parseran import read_csv
from enkripsi import decode
def login() :
    username = input("Username : ") #meminta masukkan username
    password = input("Password : ") #meminta masukkan password
    data.usernamee = username
    account_found = False
    # iterate over the rows in the users list
    agents=read_csv('user.csv')
    #mengecek apakah akun tersebut ada atau tidak, jika tidak, login gagal
    for i in range(len(agents)):
        # check if the username and password match
        if username == agents[i][1]:
            if password == decode(agents[i][2]):
                if data.login_status == "false":
                    role = agents[i][3]
                    account_found = True
                    print(f"Selamat datang, {role} {username}!")
                    print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
                    break
                elif data.login_status == "true":
                    print(f'Anda telah login dengan username {username}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.')
            else:
                account_found = True
                print("Password salah!")
                break
        else :
            account_found = False

    if not account_found :
        print("Username tidak terdaftar")
login()