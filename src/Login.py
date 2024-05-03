import data
from parseran import read_csv
from enkripsi import decode
def login() :
    username = input("Username : ") #meminta masukkan username
    password = input("Password : ") #meminta masukkan password
    account_found = False
    # iterate over the rows in the users list
    users=read_csv('user.csv')
    #mengecek apakah akun tersebut ada atau tidak, jika tidak, login gagal
    for i in range(len(users)):
        # check if the username and password match
        if username == users[i][1]:
            if password == decode(users[i][2]):
                if data.login_status == "false":
                    account_found = True
                    data.username= username
                    data.role = users[i][3]
                    data.id = int(users[i][0])
                    data.oc = int(users[i][4])
                    print(f"Selamat datang, {data.role} {username}!")
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