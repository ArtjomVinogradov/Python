from random import randint
# Harjutus 04
# Artjom Vinogradov
# 09.02.22


#Arvamismäng
nr = for i in range(1,21):
loop = 1
kordade_arv = 0

print('Arva ära number 1-20')
 
while loop == 1:
    arva = int(input('Sisesta täisarv: '))
    
    if arva == nr:
        kordade_arv += 1
        print('Tubli, pakkumisi kokku: ',kordade_arv)
        loop = 0
    elif arva < nr:
        kordade_arv += 1
        print('Sinu pakutud arv on vale u noob')
    else:
        kordade_arv += 1
        print('Sinu pakutud arv on good man')
  






#Viisikud
for i in range(1,101):
    if i%5==0:
        print(i)
   





#Pisike korrutustabel
arv = int(input("Siseta number: "))
for i in range(1,11):
   print(arv,'*',i,'=',arv*i)
   







#Paaris ja paaritu
for i in range(1,101):
    if i%2==0:
        print(i,"paaris")
    else:
        print(i,"paaritu")





#Loto
for i in range(1,6):
    print(randint(0,9),end="")
print()




#Tärnid teist version
for i in range(1,6):
    print("* "* i)

j=5
print("* "* j)






#Tärnid
def pattern(n):
      k = 5 * n - 5
      for i in range(n, -1,-1):
           for j in range(k,0,-1):
               print(end=" ")
           k = k +2
           for j in range(0, i+1):
                print("*", end=" ")
           print("\r")
pattern(5)






#jalgpalli meeskond

sugu =input("Noh kes sa oled (M/N): ")

if sugu == "M":
    vanus = int(input("Ну сколько живешь ходишь по планете? "))
    if vanus>=16 and vanus<=18:
        print("so lets goo")
    else:
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
    
    
        