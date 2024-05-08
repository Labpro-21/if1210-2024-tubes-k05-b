from parseran import read_csv,save_data
from Exit import save_oc_user_login
user_login=read_csv('user_login.csv')
user=read_csv('user.csv')
def defaultkan_data():
    user_login[1][0]=''
    user_login[1][1]=''
    user_login[1][2]=''
    user_login[1][3]=''
    user_login[1][3]='False'
    save_data('user_login.csv',user_login)

def logout() :
    if user_login[1][3]=='True':
        defaultkan_data()
        save_oc_user_login(user,user_login)
        print("Anda telah logout")
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout')
