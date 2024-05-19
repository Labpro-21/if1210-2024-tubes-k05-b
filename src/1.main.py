from Save import new_save
from Help import Help
from parseran import copy
from Login import login
from Exit import Exit
from Register import register
from Logout import logout
from Shop_Management import shop_management
from Monster_Management import monster_management
from Shop_Currency import shop_currency
from Battle import battle
from Arena import arena
from Laboratory import laboratory
from Load import load
import colorizer as clr
from Inventory import inventory
from Jackpot import jackpot
# MAIN PROGRAM
# F13
(sukses, user, user_login, monster, monster_inventory, monster_shop, item_inventory, item_shop) = load()
user_baru = copy(user)
user_login_baru = copy(user_login)
monster_baru = copy(monster)
monster_inventory_baru = copy(monster_inventory)
monster_shop_baru = copy(monster_shop)
item_inventory_baru = copy(item_inventory)
item_shop_baru = copy(item_shop)
    # if load() success
if sukses:
    print(clr.colored('\nSelamat datang di program OWCA!','green'))
    while True:
        print('\nMasukkan perintah:' + clr.colored(" (ketik 'help' untuk melihat semua perintah)", 'red', 'on_black', ['bold', 'blink']))
        menu=input('>>> ')
        """user_login[1][2]='Admin'"""
        if menu=="login":
            #F01
            login(user_baru,user_login_baru)
        elif menu=='logout':
            #F02
            logout(user_baru,user_login_baru)
        elif menu =='save':
            new_save(user_baru,user_login_baru,monster_baru,monster_shop_baru,monster_inventory_baru,item_shop_baru,item_inventory_baru)
        elif menu=="help":
            # F15
            Help(user_login_baru)
        elif menu=='exit':
            # F16
            Exit(user_baru,user_login_baru)
        elif menu=='register':
            # F16
            register(user_baru,monster_baru,monster_inventory_baru,user_login_baru)
        elif menu=='shop_management':
            if user_login_baru[1][2]=='Agent':
                print('Hak akses untuk Admin')
            else:
                shop_management(monster_shop_baru,item_shop_baru,monster_baru)
        elif menu=='monster_management':
            if user_login_baru[1][2]=='Agent':
                print('Hak akses untuk Admin')
            else:
                monster_management(monster_baru)
        elif menu=='shop_currency':
            if user_login_baru[1][2]=='Agent':
                shop_currency(monster_shop_baru,item_shop_baru,monster_inventory_baru,item_inventory_baru,user_login_baru,monster_baru)
            else:
                print('Hak akses untuk Agent')
        elif menu=='battle':
            if user_login_baru[1][2]=='Agent':
                user_login_baru = battle(user_login_baru,monster_baru,item_inventory_baru,monster_inventory_baru)
            else:
                print('Hak akses untuk Agent')
        elif menu=='arena':
            if user_login_baru[1][2]=='Agent':
                user_login_baru = arena(user_login_baru,monster_baru)
            else:
                print('Hak akses untuk Agent')
        elif menu=='laboratory':
            if user_login_baru[1][2]=='Agent':
                laboratory(user_login_baru,monster_baru,monster_inventory_baru)
            else:
                print('Hak akses untuk Agent')
        elif menu=='jackpot':
            if user_login_baru[1][2]=='Agent':
                (monster_inventory_baru,user_login_baru)=jackpot(user_login_baru,monster_baru,monster_inventory_baru)
            else:
                print('Hak akses untuk Agent')
        elif menu=='inventory':
            if user_login_baru[1][2]=='Agent':
                inventory(user_login_baru,monster_baru,item_inventory_baru,monster_inventory_baru)
            else:
                print('Hak akses untuk Agent')
        else:
            print('Tidak ada perintah')
