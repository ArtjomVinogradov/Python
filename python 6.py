# Artjom Vinogradov
#  03.03.2022
#    IT-21


#Erakonnad

erakonnad = []
KE = 0
RE = 0
IRL = 0
SDE = 0

print(f"{'Eesnimi'}  {'Perekonnaimi'}  {'Erakond'}  {'Number'}  ")

with open('EKRE.txt', 'r') as my_fail:
    for rida in my_fail:
        for i in (rida):
            eesnimi, perenimi, erakond, number = (rida.split(" "))
        print(f"{eesnimi} {perenimi} {erakond} {number}")
        if erakond == "RE":
            RE += 1
        elif erakond == "KE":
            KE += 1
        elif erakond == "IRL":
            IRL += 1
        elif erakond == "SDE":
            SDE += 1
        
    if erakond not in erakonnad:
            erakonnad.append(erakond)
        
    with open('Resultat.txt','a') as fail_missalvestab:
        fail_missalvestab.write(str(eesnimi)+" "+str(perenimi)+'\n')


print()
print(f"Reformi Erakond: {RE}")
print(f"Kesk Erakond: {KE}")
print(f"Sotsiaaldemokraadid: {SDE}")
print(f"Isamaa Erakond: {IRL}")
print(f"Erakonnad kokku: {len(erakonnad)}")