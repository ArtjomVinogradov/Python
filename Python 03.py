# Harjutus 3
# A. Vinogradov
# 03.02.2022



#Palindroom
 # function to check string is
# palindrome or not
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
start = input("Algusaeg: ")
lopp =input("Lõpuaeg: ")
#tükeldus
hh1,mm1 = start.split(":")
hh2,mm2 = lopp.split(":")
#teisendamine minutiteks
minutid = int(hh1)*60+int(mm1)
minutid2 = int(hh2)*60+int(mm2)
#absoluutväärtus
ajavahe = abs(minutid-minutid2)
#teisendamine hh:mm
hh = ajavahe // 60 #täisarvuline jagamine
mm = ajavahe % 60 #jääk
#lause formindamine format abil
print(f"Õpilase päeva pikkus on {hh}:{mm}")






#emaili kontroll
#TRUE/FALSE
email = input("sinu email: ")
print("@" in email)





#vandumine
vanne = input("а как ты хотел все по чесноку: ")
vanne = vanne.lower().replace("kurat","***")
print(vanne)




#korralik kasutajanimi
nimi = input("Siseta nimi: ")
nimi = nimi.capitalize().strip()
#nimi = nimi.
print("Tere "+nimi+"!")