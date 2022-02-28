# Artjom Vinogradov
#  21.02.2022
#    IT-21



#Ruumalade leidmise programm
import math


def kuubiRuumala(a):
    v=a**3
    return v

def keraRuumala(a):
    v=(4*math.pi*a**3)/3
    return v

def kolmnRuumala(a,h):
    v=(math.pi*a**2*h)/3
    return v

def silinderRuumala(r,h):
    v=math.pi*r**2*h
    return v


number=0
loop=0
while loop == 0:
    kujund = int(input("Vali kujund\n 1) Kuup\n 2) Kera\n 3) Koonus\n 4) Silinder\n 5) Lõpeta\n Sisesta soovitud number: "))

    if kujund==1:
        number = int(input("Valisid kuubi siis sisesta kuubi küljepikkus:  "))
        print(f"Kuubi ruumala on: {kuubiRuumala(number)}")
    
    elif kujund==2:
        number = int(input("Valisid kera siis sisesta kera raadius:  "))
        print(f"Kera ruumala on: {keraRuumala(number)}")
    
    elif kujund==3:
        number = int(input("Valisid koonuse siis sisesta koonuse raadius:  "))
        number2 = int(input("Sisesta koonuse kõrgus:  "))
        print(f"Koonuse ruumala on: {kolmnRuumala(number,number2)}")
    
    elif kujund==4:
        number = int(input("Valisid silindri siis sisesta silindri raadius:  "))
        number2 = int(input("Sisesta silindri kõrgus:  "))
        print(f"Silindri ruumala on: {silinderRuumala(number,number2)}")
    else:
        loop=1  



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