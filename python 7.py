import math
# Artjom Vinogradov
#  21.02.2022
#    IT-21


#Ruumalade leidmise programm

def kuub(a):
    v=a**3
    return v

def kera(a):
    v=(4*math.pi*a**3)/3
    return v

def kolmn(a,h):
    v=(math.pi*a**2*h)/3
    return v

def silinder(r,h):
    v=math.pi*r**2*h
    return v


arv=0
loop=0
while loop == 0:
    tehe = int(input("Vali tehe\n 1) Kuub\n 2) Kera\n 3) Koonus\n 4) Silinder\n 5) Lõpeta\n Sisesta tehe: "))

    if tehe==1:
        arv = int(input("Sa valisid kuub, sisesta kuubi küljepikkus:  "))
        print(f"Kuubi ruumala on: {kuub(arv)}")
    
    elif tehe==2:
        arv = int(input("Sa valisid kera, sisesta kera raadius:  "))
        print(f"Kera ruumala on: {kera(arv)}")
    
    elif tehe==3:
        arv = int(input("Sa valisid koonuse, sisesta koonuse raadius:  "))
        arv2 = int(input("Sisesta koonuse kõrgus:  "))
        print(f"Koonuse ruumala on: {kolmn(arv,arv2)}")
    
    elif tehe==4:
        arv = int(input("Sa valisid silindri, sisesta silindri raadius:  "))
        arv2 = int(input("Sisesta silindri kõrgus:  "))
        print(f"Silindri ruumala on: {silinder(arv,arv2)}")
    else:
        loop=1  



#funktsioon

nimi = "Mees"
keel = input("Sisestage keel EST/ENG: ")

def Tervitamine(nimi,keel):
    "Tervitamine"
    if keel == "EST":
        tervitus = print(f"Tere {nimi}")
    elif keel == "ENG":
        tervitus = print(f"Hello {nimi}")
    else:
         tervitus = print(f"Привет {nimi}")
    return tervitus
#funktsiooni välja
print(Tervistamine)
