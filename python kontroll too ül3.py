#Noh ei saanud mitte midagi proovisin aga ei saanud noh siis see on teie valik
#mis mulle panna aga Ma arvan, et oleks võimalik panna kolme et ma püütsin seda teha
#vot niimodi
#edu teile nägemist!



import random
# Artjom Vinogradov
#  10.03.2022
#    IT-21


#Tehteid                              -              +
tehe = int(input("Vali tehe\n 1) lahutamine\n 2) liitmine\n Sisesta tehe: "))

if tehe==1:
        arv = print("Sa valisid lahutamine, noh siis alustame: ")
        
def randomCalc():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '/':operator.truediv}
    num1 = random.randint(0,12)
    num2 = random.randint(1,10)   # I don't sample 0's to protect against divide-by-zero
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1,num2)
    print('What is {} {} {}?\n'.format(num1, op, num2))
    return answer










arv1=int(input("Mis sa arvad 11-6 = "))
if arv1==5:
    print ("Õige")
    õige1=int(1)
else:
    print ("Vale, vastus on: 5")
    õige1=int(0)

arv2=int(input("Mis sa arvad 7-3 = "))
if arv2==4:
    print ("Õige")
    õige2=int(1)
else:
    print ("Vale, vastus on: 4")
    õige2=int(0)
        
arv3=int(input("Mis sa arvad 18-2 = "))
if arv3==16:
    print ("Õige")
    õige3=int(1)
else:
    print ("Vale, vastus on: 16 = ")
    õige3=int(0)

arv4=int(input("Mis sa arvad 57-12 = "))
if arv4==45:
    print ("Õige")
    õige4=int(1)
else:
    print ("Vale, vastus on: 45")
    õige4=int(0)

arv5=int(input("Mis sa arvad 31-12 = "))
if arv5==19:
    print ("Õige")
    õige5=int(1)
else:
    print ("Vale, vastus on: 15")
    õige5=int(0)

arv6=int(input("Mis sa arvad 67-20 = "))
if arv6==47:
    print ("Õige")
    õige6=int(1)
else:
    print ("Vale, vastus on: 47")
    õige6=int(0)

arv7=int(input("Mis sa arvad 14-5 = "))
if arv7==9:
    print ("Õige")
    õige7=int(1)
else:
    print ("Vale, vastus on: 9")
    õige7=int(0)
    
arv8=int(input("Mis sa arvad 8-4 = "))
if arv8==4:
    print ("Õige")
    õige8=int(1)
else:
    print ("Vale, vastus on: 4")
    õige8=int(0)
    
arv9=int(input("Mis sa arvad 100-5 = "))
if arv9==95:
    print ("Õige")
    õige9=int(1)
else:
    print ("Vale, vastus on: 95")
    õige9=int(0)
    
arv10=int(input("Mis sa arvad 9-8 = "))
if arv10==1:
    print ("Õige")
    õige10=int(1)
else:
    print ("Vale, vastus on: 1")
    õige10=int(0)

õiged=õige1+õige2+õige3+õige4+õige5+õige6+õige7+õige8+õige9+õige10
print("Õiged vastused: %s/10" %(õiged))

per=int(õiged/10*100)

if per>=50:
    print("Väga hea, sa sai selle töö valmis %s Procent" % (per))
else:
    print("Oh kurat mees, ära anna alla järgmine kord tee valmis %s Procent " %(per)) 

            
            



if tehe==2:
        arv = print("Sa valisid liitmine, noh siis alustame: ")

#Korrutamine kontroll

print("Oled kindel et tahad testima? See on päris raske tegelikult")

arv1=int(input("Mis sa arvad 15+1 = "))
if arv1==16:
    print ("Õige")
    õige1=int(1)
else:
    print ("Vale, vastus on: 16")
    õige1=int(0)

arv2=int(input("Mis sa arvad 7+2 = "))
if arv2==9:
    print ("Õige")
    õige2=int(1)
else:
    print ("Vale, vastus on: 9")
    õige2=int(0)
        
arv3=int(input("Mis sa arvad 12+15 = "))
if arv3==27:
    print ("Õige")
    õige3=int(1)
else:
    print ("Vale, vastus on: 27 = ")
    õige3=int(0)

arv4=int(input("Mis sa arvad 57+3 = "))
if arv4==60:
    print ("Õige")
    õige4=int(1)
else:
    print ("Vale, vastus on: 60")
    õige4=int(0)

arv5=int(input("Mis sa arvad 3+12 = "))
if arv5==15:
    print ("Õige")
    õige5=int(1)
else:
    print ("Vale, vastus on: 15")
    õige5=int(0)

arv6=int(input("Mis sa arvad 6+7 = "))
if arv6==13:
    print ("Õige")
    õige6=int(1)
else:
    print ("Vale, vastus on: 13")
    õige6=int(0)

arv7=int(input("Mis sa arvad 5+14 = "))
if arv7==19:
    print ("Õige")
    õige7=int(1)
else:
    print ("Vale, vastus on: 19")
    õige7=int(0)
    
arv8=int(input("Mis sa arvad 5+8 = "))
if arv8==13:
    print ("Õige")
    õige8=int(1)
else:
    print ("Vale, vastus on: 13")
    õige8=int(0)
    
arv9=int(input("Mis sa arvad 100+5 = "))
if arv9==105:
    print ("Õige")
    õige9=int(1)
else:
    print ("Vale, vastus on: 105")
    õige9=int(0)
    
arv10=int(input("Mis sa arvad 9+8 = "))
if arv10==17:
    print ("Õige")
    õige10=int(1)
else:
    print ("Vale, vastus on: 17")
    õige10=int(0)

õiged=õige1+õige2+õige3+õige4+õige5+õige6+õige7+õige8+õige9+õige10
print("Õiged vastused: %s/10" %(õiged))

per=int(õiged/10*100)

if per>=50:
    print("Väga hea, sa sai selle töö valmis %s Procent" % (per))
else:
    print("Oh kurat mees, ära anna alla järgmine kord tee valmis %s Procent " %(per)) 
    
    
    
    
    

