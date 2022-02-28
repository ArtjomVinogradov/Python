# Artjom Vinogradov
#  26.02.2022
#    IT-21



#eestistatud kuupäev
import datetime

aeg = datetime.datetime.now()                                                                  #1980-11-06 17:32:56
print(aeg.strftime("%d veebruar %Y aasta"))


#isikukood
kood = 50511020991
aasta = int(kood[1]+kood[2])+2000
kuu = int(kood[3]+kood[4])
päev = int(kood[5]+kood[6])




