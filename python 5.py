# Artjom Vinogradov
#  18.02.2022
#    IT-21



#Tärnid

numbrid = [23,63,72,10,24,98]

for i in range(len(numbrid)):
    print("*" * numbrid[i])
print()






#Vanused

numbrid = [23,63,72,10,24,98]

print(f"kõige vanem: {max(numbrid)}")
print(f"noorem: {min(numbrid)}")
print(f"summa: {sum(numbrid)}")
print(f"keskmine: {sum(numbrid)/len(numbrid):10.2f}")

print()




#Duplikaadid

print()
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
p_opilased = []

for i in range(len(opilased)):
    if opilased[i] not in p_opilased:
        p_opilased.append(opilased[i])
for i in range(len(p_opilased)):
    print(p_opilased[i])









#Opilased

print()

opilased = ["Juhan","Kati","Maarja","Mario","Mati"]

for i in range(len(opilased)):
    print(f"{i+0} {opilased[i]}")
muutmine = int(input("Mis nimi sa tahad muuda? (0/1/2/3/4): "))
del opilased[muutmine-0]
nimed = input("Sisestage uus nimed: ")
opilased.insert(muutmine-0,nimed)
for j in range(len(opilased)):
    print(opilased[j])
    








# Nimed

nimed = []

for i in range(5):
    nimi = input("Sisesta nimi:  ")
    nimed.append(nimi)
nimed.sort()
for e in range(len(nimed)):
    print(nimed[e])
