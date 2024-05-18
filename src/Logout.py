import parseran
import Exit
def defaultkan_data():
    user_login=parseran.read_csv('user_login.csv')
    user_login[1][0]=''
    user_login[1][1]=''
    user_login[1][2]=''
    user_login[1][3]=''
    user_login[1][4]='False'
    parseran.save_data('user_login.csv',user_login)

def logout(user:list,user_login:list) :
    if user_login[1][4]=='True':
        defaultkan_data()
        Exit.save_oc_user_login(user,user_login)
        print("Anda telah logout")
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout')
