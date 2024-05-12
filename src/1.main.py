from Save import new_save
from Help import Help
from parseran import read_csv
from Login import login
from Exit import Exit
from Logout import logout
from Shop_Management import shop_management
from Monster_Management import monster_management
from Shop_Currency import shop_currency
from Battle import battle
from Arena import arena
from Laboratory import lab
from Load import loading,read_csv_files
import colorizer as clr
from Inventory import inventory
# MAIN PROGRAM
# F13
folder = loading()
if folder:
    user, monster, monster_shop, monster_inventory, item_shop, item_inventory = read_csv_files(folder)
user_login = read_csv('user_login.csv')
# if load() success
while True:
    print('Masukkan perintah:' + clr.colored(" (ketik 'help' untuk melihat semua perintah)", 'red', 'on_black', ['bold', 'blink']))
    menu=input('>>> ')
    if menu=="login":
        #F01
        login()
    elif menu=='logout':
        #F02
        logout()
    elif menu =='save':
        new_save()
    elif menu=="help":
        # F15
        Help()
    elif menu=='exit':
        # F16
        Exit()
    elif menu=='shop_management':
        if user_login[1][2]=='Agent':
            print('Hak akses untuk Admin')
        else:
            shop_management()
    elif menu=='monster_management':
        if user_login[1][2]=='Agent':
            print('Hak akses untuk Admin')
        else:
            monster_management()
    elif menu=='shop_currency':
        if user_login[1][2]=='Agent':
            shop_currency()
        else:
            print('Hak akses untuk Agent')
    elif menu=='battle':
        if user_login[1][2]=='Agent':
            battle()
        else:
            print('Hak akses untuk Agent')
    elif menu=='arena':
        if user_login[1][2]=='Agent':
            arena()
        else:
            print('Hak akses untuk Agent')
    elif menu=='laboratory':
        if user_login[1][2]=='Agent':
            lab()
        else:
            print('Hak akses untuk Agent')

