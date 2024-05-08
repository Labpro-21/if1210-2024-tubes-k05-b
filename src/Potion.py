from parseran import read_csv
from monster import edit_att_m
user_login=read_csv('user_login.csv')
item_inv=read_csv('item_inventory.csv')
monster_inv=read_csv('monster_inventory.csv')
monster=read_csv('monster.csv')
data_id=user_login[1][0]
data_m = edit_att_m
data_p = []
#strength ningkatin 5% atk
#resilience ningkatin 5% def (tapi klo defnya mentok 50)
#healing mengsi darah sebanyak 25% dari base hp klo diserang
#mentoknya harus di base hpnya(pas udah ditaambahin)
def load_data_p():
    for p in item_inv:
        if p[0]==data_id:
            data_p.append([p[0],p[1]])
    return data_p

def use_p():
    data_po= load_data_p()
    for p in data_po:
        if int(p[1])>0:
            


            