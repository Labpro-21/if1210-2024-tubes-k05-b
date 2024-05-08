from parseran import read_csv
monster_inv=read_csv('monster_inventory.csv')
monster=read_csv('monster.csv')
user_login=read_csv('user_login.csv')
data_id = user_login[1][0]
edit_att= {
    "id": [],
    "type": [],
    "atk": [],
    "def": [],
    "hp": [],
}

def edit_att_m():
    for m in monster_inv:
        if m[0]==data_id:
            edit_att["id"].append(m[1])
            lvl=int(m[2])
            if m[2]=='1':
                for mo in monster:
                    if mo[0]==m[1]:
                        edit_att["type"].append(mo[1])
                        edit_att["atk"].append(int(mo[2]))
                        edit_att["def"].append(int(mo[3]))
                        edit_att["hp"].append(int(mo[4]))
            else:
                for mo in monster:
                    if mo[0]==m[1]:
                        edit_att["type"].append(mo[1])
                        edit_att["atk"].append(int(mo[2])+int(mo[2])*(lvl-1)*0.1)
                        if int(mo[3])+int(mo[3])*(lvl-1)*0.1<=50:
                            edit_att["def"].append(int(mo[3])+int(mo[3])*(lvl-1)*0.1)
                        else:
                            edit_att["def"].append(50)
                        edit_att["hp"].append(int(mo[4])+int(mo[4])*(lvl-1)*0.1)
    return edit_att
print(edit_att_m())
