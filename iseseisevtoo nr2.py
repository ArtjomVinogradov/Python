import random

õiged = 0
tehe = random.randint(1,2)
a = random.randint(1,10)
b = random.randint(1,10)


for i in range(10):

    if tehe==1:
        prod = a + b
        vastus = int(input(f"okay lets go man: {a}+{b}= "))
        
        if vastus==prod:
            print("õige")
            õige1=int(1)
        else:
            print("vale")
            õige1=int(0)
    
    if tehe==2:
        prod = a - b
        vastus = int(input(f"noh vaatame kuidas sa lahutad: {a}-{b}= "))
       
        if vastus==prod:
            print("õige")
            õige2=int(1)
        else:
            print("vale")
            õige2=int(0)
            
            
õiged=õige1+õige2
print("Õiged vastused: %s/10" %(õiged))

per=int(õiged/10*100)

if per>=50:
    print("Väga hea, sa sai selle töö valmis %s Procent" % (per))
else:
    print("Oh kurat mees, ära anna alla järgmine kord tee valmis %s Procent " %(per))