from Type import effective as eff
from commands import save

print(">>> EXIT")
def exit (user:eff, monster:eff, potion:list[list]):
    konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    while not ((konfirmasi == "y") or (konfirmasi == "Y") or (konfirmasi == "n") or (konfirmasi == "N")):
        konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        
    if (konfirmasi == "y") or (konfirmasi == "Y"):
        save(user, monster, potion)
        exit()
    else:
        exit()