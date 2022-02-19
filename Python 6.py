# Artjom Vinogradov
#  19.02.2022
#    IT-21


#ülesanne 6

erakonnad = []
kesk = 0
ref = 0                                      #Vali EKRE
print(f"{'Eesnimi'} {'Perekonnaimi'} {'Erakond'} {'Number'}  ")

with open('EKRE.txt', 'r') as minu_fail:
    for rida in minu_fail:
        for i in (rida):
            enimi, pnimi, erakond, number = (rida.split(" "))
        print(f"{enimi} {pnimi} {erakond} {number}")
        if erakond == "RE":
            ref += 1
        elif erakond == "KE":
            kesk += 1
        
        if erakond not in erakonnad:
            erakonnad.append(erakond)
        with open('Result.txt','a') as fail_kirjutamiseks:
            fail_kirjutamiseks.write(str(enimi)+" "+str(pnimi)+'\n')


print( )
print(f"reformikad: {ref}")
print(f"keskmised: {kesk}")
print(f"Erakondi kokku: {len(erakonnad)}")

