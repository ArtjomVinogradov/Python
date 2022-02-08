
# Harjutus 04
# Artjom Vinogradov
# 08.02.22


#jalgpalli meeskond

sugu = int(input("Noh kes sa oled (M/N): "))

if sugu == "M":
    vanus = int(input("Ну сколько живешь ходишь по планете?"))
    if vanus>=16 and vanus<=18:
        print("so lets goo")
    else :
        print("No your are too old or too young")
else:
    print("Naised ei sobi")



    






#Müük
hind = int(input("Siseta toode hind: "))
if hind<=10:
    ale = 0.1
else:
    ale = 0.2
hind = hind-hind*ale
print("hind on",hind,"eurot")








#juubel
arv1 = int(input("Ну сколько живешь ходишь по планете?"))
p, k, a = arv1.plit(".")
vanus = 2022- int(a)
jaak = vanus%5
if jaak==0:
    print("Вау юбилей класс")
else:
    print=("Ну все иди гуляй нет юбилей сщегол")









#matemaatika
arv1 = int(input("sisesta arv"))
arv2 = int(input("sisesta arv mis sa ootad?"))
tehe = int(input("vali tehe:\n 1) liitmine\n 2) lahutamine\n 3) jagamine\n 4) korrutamine\n"))
if tehe==1:
    vastus = arv1+arv2
elif tehe==2:
    vastus = arv1-arv2
elif tehe==3:
    vastus = arv1/arv2
elif tehe==4:
    vastus = arv1*arv2
print(vastus)






#Ruudu kontroll ==> < >= >= !=
a = int(input("Sisesta ruudu üks külg: "))
b = int(input("Sisesta ruudu teine külge: "))
if a == b:
    print("Tegemist on ruuduga")
#elif:
#     dsadasfd
else:
    print("Risttahukas")
    
    
        