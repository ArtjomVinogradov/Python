# Iseseisev töö
# Artjom Vinogradov
# IT-21
# 01.03.22


#Korrutamise kontrollimineKorrutamise kontrollimine
arv1=int(input("Mis sa arvad 5*1 = "))
if arv1==5:
    print ("Õige")
    õige1=int(1)
else:
    print ("Vale, vastus on: 5")
    õige1=int(0)

arv2=int(input("Mis sa arvad 7*2 = "))
if arv2==14:
    print ("Õige")
    õige2=int(1)
else:
    print ("Vale, vastus on: 14")
    õige2=int(0)
        
arv3=int(input("Mis sa arvad 12*2 = "))
if arv3==24:
    print ("Õige")
    õige3=int(1)
else:
    print ("Vale, vastus on: 24 = ")
    õige3=int(0)

arv4=int(input("Mis sa arvad 57*3 = "))
if arv4==171:
    print ("Õige")
    õige4=int(1)
else:
    print ("Vale, vastus on: 171")
    õige4=int(0)

arv5=int(input("Mis sa arvad 3*12 = "))
if arv5==36:
    print ("Õige")
    õige5=int(1)
else:
    print ("Vale, vastus on: 36")
    õige5=int(0)

arv6=int(input("Mis sa arvad 6*7 = "))
if arv6==42:
    print ("Õige")
    õige6=int(1)
else:
    print ("Vale, vastus on: 42")
    õige6=int(0)

arv7=int(input("Mis sa arvad 5*14 = "))
if arv7==70:
    print ("Õige")
    õige7=int(1)
else:
    print ("Vale, vastus on: 70")
    õige7=int(0)
    
arv8=int(input("Mis sa arvad 5*8 = "))
if arv8==40:
    print ("Õige")
    õige8=int(1)
else:
    print ("Vale, vastus on: 40")
    õige8=int(0)
    
arv9=int(input("Mis sa arvad 100*5 = "))
if arv9==500:
    print ("Õige")
    õige9=int(1)
else:
    print ("Vale, vastus on: 500")
    õige9=int(0)
    
arv10=int(input("Mis sa arvad 9*8 = "))
if arv10==72:
    print ("Õige")
    õige10=int(1)
else:
    print ("Vale, vastus on: 72")
    õige10=int(0)

õiged=õige1+õige2+õige3+õige4+õige5+õige6+õige7+õige8+õige9+õige10
print("Õiged vastused: %s/10" %(õiged))

per=int(õiged/10*100)

if per>=50:
    print("Väga hea, sa sai selle töö valmis %s Procent" % (per))
else:
    print("Oh kurat mees, ära anna alla järgmine kord tee valmis %s Procent " %(per)) 


