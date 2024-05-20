
#strength ningkatin 5% atk
#resilience ningkatin 5% def (tapi klo defnya mentok 50)
#healing mengsi darah sebanyak 25% dari base hp klo diserang
#mentoknya harus di base hpnya(pas udah ditaambahin)
def load_data_p(item_inv:list,user_login:list)->list:
    data_id=user_login[1][0]
    data_p = []
    for p in item_inv:
        if p[0]==data_id:
            data_p.append([p[1],p[2]])
    return data_p


            