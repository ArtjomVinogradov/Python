# Artjom Vinogradov
#  03.03.2022
#    IT-21



#Tärnid

nummer = [66,45,38,41,95,102]

for i in range(len(nummer)):
    print("*" * nummer[i])
print()




#Vanus

numbrid = [15,31,56,72,43,100]

print(f"kõige vanem: {max(numbrid)}")
print(f"kõige noorem: {min(numbrid)}")
print(f"summa kokku: {sum(numbrid)}")
print(f"keskmine vanus: {sum(numbrid)/len(numbrid):10.2f}")
print()




#Duplikaadid

print()
õpilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
muuda_õpilased = []

for i in range(len(õpilased)):
    if õpilased[i] not in muuda_õpilased:
        muuda_õpilased.append(õpilased[i])

for j in range(len(muuda_õpilased)):
    print(muuda_õpilased[j])





#Õpilased
print()

õpilased = ["Juhan","Kati","Maarja","Mario","Mati"]

for i in range(len(õpilased)):
    print(f"{i+0} {õpilased[i]}")
muutus = int(input("Mis nimi tahad muuta? (0/1/2/3/4): "))

del õpilased[muutus-0]
nimed = input("Siseta uus nimi: ")
õpilased.insert(muutus-0,nimed)


for j in range(len(õpilased)):
    print(õpilased[j])
    


# Nimed

nimed = []

for i in range(5):
    nimi = input("Sisesta nimi:  ")
    nimed.append(nimi)
nimed.sort()
for j in range(len(nimed)):
    print(nimed[j])