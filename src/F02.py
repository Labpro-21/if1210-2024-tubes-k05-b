import argparse
import os
from Type import effective as eff

# len matrix with mark
def mtx_len(matrix:list, mark:list, iterate:int) -> int:
    # iterate=0
    if matrix[iterate]==mark:
        return iterate
    else:
        return mtx_len(matrix,mark,iterate+1)

# read csv
def read_csv(path_csv:str) -> tuple[list,int]:
    # asumsi csv selalui diakhiri newline
    file = open("src/user.csv",'r')
    # count line
    count=0

    for line in file:
        # header
        if count==0:
            count+=1

            # determine len arr needed to store the string
            count_delimiter=0
            for char in line:
                if char==";":
                    count_delimiter+=1
            # initialization of mtx
            mtx=[["" for i in range (count_delimiter+1)] for i in range (200)]
            mtx_idx=count-1

        # not header
        else:
            str_temp=""
            arr_temp=["" for i in range (count_delimiter+1)]
            # indexing for arr_temp
            arr_idx=0
            mtx_idx=count-1

            for char in range (len(line)):
                if line[char]==";" or line[char]=="\n":
                    arr_temp[arr_idx]=str_temp
                    arr_idx+=1
                    str_temp=""
                else:
                    str_temp+=line[char]

            mtx[mtx_idx]=arr_temp
            count+=1
        
    # csv hanya berisi header: mtx_idx=0
    # asumsi csv diakhiri newline
    if mtx[mtx_idx-1]==["" for i in range (count_delimiter+1)]:
        mtx_idx-=1
    
    mtx[mtx_idx+1]=["MARK" for i in range(count_delimiter+1)]
   
    return (mtx, mtx_len(mtx,["MARK" for i in range (count_delimiter+1)], 0))

def login (users : eff, user_now : str, role_now : str) -> tuple [str, str, bool]:
    # decoration
    print(">>> LOGIN")

    # cek login status
    if role_now == "":
        belum_login = True
    else : 
        belum_login = False
    
    if (belum_login):
        username = input("Username : ")
        password = input("Password : ")
        
        username_ada = False
        password_ada = False
        
        # matrix_user : [username, password, role]
        matrix_user = users.mtx
        len_user = users.NEff
        
        # find username in matrix
        for i in range (len_user):
            if (matrix_user[i][0] == (username)):
                username_ada = True
        
        # confirm password
        if username_ada == True:
            for i in range (len_user):
                if (matrix_user[i][1] == (password)):
                    password_ada = True
                    index = i
                else: # not(username_ada)
                    print() # dekorasi
                    print("Username tidak terdaftar!")
                    
        # after searching and confirming
        if (username_ada == True) and (password_ada == True):
            # cek role
            if matrix_user[i][4] == 'Admin':
                role = 'Admin'
            elif matrix_user[i][4] == 'Agent':
                role = 'Agent'
            print(f"Selamat datang, {role} {matrix_user[i][2]}!")
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")

            belumlogin = False
            role_now = matrix_user[index][2]
            user_now = username

        elif (username_ada == True) and (password_ada == False):
            print() # dekorasi
            print("Password salah!")            
        
    else : #belum_login == False
        print("Login gagal!")
        print(f"Anda telah login dengan username {user_now}, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.")
        
    return (user_now, role_now, not(belumlogin))
