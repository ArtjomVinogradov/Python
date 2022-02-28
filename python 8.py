# Artjom Vinogradov
#  26.02.2022
#    IT-21



#Esimene auto
class Auto1:
    #atribuudid
    nimi = 'teadmata'
    vanus = 0
    hind = 'teadmata'
    mootor = 0
    
    
    #meetodid
    def __init__(self,x,y):
        self.nimi = x
        self.vanus = y
       
        
    def kuva(self):
        print('Nimi: {} \nVanus: {}'.format(self.nimi, self.vanus))
        
    def lisahind(self,x):
        self.hind = x
        
    def lisamootor(self,x):
        self.mootor = x
        
    def kuvamootor(self):
        print('Mootor: {}'.format(self.mootor))
        
    def kuvahind(self):
        print('Hind: {}'.format(self.hind))
        

uusObjekt = Auto1("Volkswagen (Touareg)", 2018)
uusObjekt.lisahind('50 900€ "auto24.ee"')
uusObjekt.kuva()
uusObjekt.kuvahind()
uusObjekt.lisamootor("3.0 TDI 210kW")
uusObjekt.kuvamootor()





#Teine auto
class Auto2:
    #atribuudid
    nimi = 'teadmata'
    vanus = 0
    hind = 0
    mootor = 'teadmata'
    
    
    #meetodid
    def __init__(self,x,y):
        self.nimi = x
        self.vanus = y
       
        
    def kuva(self):
        print('Nimi: {} \nVanus: {}'.format(self.nimi, self.vanus))
        
    def lisahind(self,x):
        self.hind = x
        
    def lisamootor(self,x):
        self.mootor = x
        
    def kuvamootor(self):
        print('Mootor: {}'.format(self.mootor))
        
    def kuvahind(self):
        print('Hind: {}'.format(self.mootor))
        

uusObjekt = Auto1("BMW X5", 2018)
uusObjekt.lisahind('49 900€ "auto24.ee"')
uusObjekt.kuva()
uusObjekt.kuvahind()
uusObjekt.lisamootor("3.0 TDI 190kW")
uusObjekt.kuvamootor()