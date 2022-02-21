# Artjom Vinogradov
#  21.02.2022
#    IT-21



#Ruumalade leidmise programm

kujund = int(input("Vali mingi kujund\n 1) Kuup\n 2) Kera\n 3) Koonus\n 4) Silinder\n Siseta kujundi number: "))
def ruumala(kujund,number):
    if kujund==1:
        number = int(input("Sa valisid kuubi. Siseta kuubi pikkus: "))
        print(f"kuubi ruumala on: {number*number*number}")
    elif kujund==2:
        number = int(input("Sa valisid kera. Siseta kera raadius: "))
        print(f"kera raadius on: {4*(number*(number*3,14))}")
    elif kujund==3:
        number = int(input("Sa valisid koonus. Siseta koonus raadius: "))
        print(f"koonus raadius on: {4*(number*(number*3,14))}")
        



#funktsioon
'''
nimi = "Geralt"
keel = "EST"

def Tervistamine(nimi,keel):
    "Tervitamine"
    if keel == "EST"
        tervitus = (f"Tere {nimi}")
    elif keel == "ENG"
        tervistus = (f"Hello {nimi}")
    else:
         tervistus = (f"Привет {nimi}")
    return tervistus
#funktsiooni välja
print(Tervistamine(nimi,keel))
'''