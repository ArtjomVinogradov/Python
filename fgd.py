#Simo Andreas
def kuu_nimi(a):
    kuud=["","jaan","veeb","mär","aprill"]
    return kuud[a]
print(kuu_nimi(1))

def kuupaev_sonena(b)
    dd,mm,yyyy=b.split(".")
    print(dd,kuu_nimi(int(mm)),yyyy)
    
kuupaev_sonena("24.02.1918")





#Martin 4.5

def pkarv(a):
    fail = open(a, encoding="UTF-8")
    for i in fail:
        if int(i)<6:
            summa+=(i)
        return summa
print("hoiupörsasse läheb",pkarv("mundid.txt"),"senti")
            






#Sten Veski 4.4

kulalised = int(input("Mitu külalist tuleb?:"))
def tervitus(a):
    for i in range(a):
        print(i+1)
tervitus(kulalised)






#Erik Teppan
def eelarve(a):
    summa = a*10+55
    return summa
kutsutud = int(input("Mitu inimest tuleb?: "))
tuleb = int(input("Kindalt tuleb: "))
print("Maksimaalne eelarve:",eelarve(kutsutud),"€")
print("Maksimaalne eelarve:",eelarve(tuleb),"€")




#Matis Russi 4.2

def mahlapakkide_arv(kogus):
    mahlapakkidearv = round(kogus*0.4/3,0)
    return mahlapakkidearv
kg = int(input("Sisesta õunte kogus: "))
print(int(mahlapakkide_arv(kg)))
 

#Kristo Tammeleht 4.1
kuva = int(input("Mitu korda soovid kuvada? "))
def banner(t,k):
    for i in range(k):
        print(t.upper())
        
banner("Osta ka sa ei kahetse!")