import re
# Artjom Vinogradov
#  02.03.2022
#    IT-21


#Otsin IP addresses

ip=" "

with open('nuloorem.txt', 'r') as fail:
    for line in fail:
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",line):
            print(line,end="")



#Otsin paroolid

with open('nuloorem.txt', 'r') as fail:
    for line in fail:
        if re.findall("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$",line):
            print(line,end="")