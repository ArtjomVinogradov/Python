import random

õiged = 0



for i in range(3):

    tehe = random.randint(1,2)
    a = random.randint(1,10)
    b = random.randint(1,10)
    if tehe==1:
        prod = a + b
        vastus = int(input(f"okay lets go man: {a}+{b}= "))
        
        if vastus==prod:
            print("õige")
            õiged+=1
        else:
            print("vale")
            

    if tehe==2:
        prod = a - b
        vastus = int(input(f"noh vaatame kuidas sa lahutad: {a}-{b}= "))
       
        if vastus==prod:
            print("õige")
            õiged+=1
        else:
            print("vale")
            
           

print("Õiged vastused: %s/10" %(õiged))

per=int(õiged/10*100)

if per>=50:
    print(f"Väga hea, sa sai selle töö valmis{per} %")
else:
    print(f"Oh kurat mees, ära anna alla järgmine kord tee valmis {per} % ")