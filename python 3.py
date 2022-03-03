# Harjutus 3
# Artjom Vinogradov
# 03.02.2022



#Palindroom

def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")




#tundide ajad
start = input("Alustamine aeg: ")
stop =input("Lõpuaeg: ")
#tükeldus
h1,m1 = start.split(":")
h2,m2 = stop.split(":")
#teisendamine minutiteks
minutid1 = int(h1)*60+int(m1)
minutid2 = int(h2)*60+int(m2)
#absoluutväärtus
ajavahe = abs(minutid1-minutid2)
#teisendamine hh:mm
hh = ajavahe // 60 #täisarvuline jagamine
mm = ajavahe % 60 #jääk
#lause formindamine format abil
print(f"Õpilase päeva pikkus on {hh}:{mm}")




#Email
email = input("sinu email: ")
print("@" in email)



#vandumine
vandumine = input("а как ты хотел все по чесноку: ")
vandumine = vandumine.lower().replace("kurat","***")
print(vanne)



#Korralik nimi
nimi = input("Siseta nimi: ")
nimi = nimi.capitalize().strip()
print("Tere "+nimi+"!")