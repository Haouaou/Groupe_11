# -*- coding: utf-8 -*-
# ADOUM ABBAKAKA ABDRAMAN 17B523FS
     #CHEF D'AGENCE
class Compte_agence:
    #CONSTRUCTEUR
    def __init__(self,solde):
        self.solde=solde
    #LES FONCTIN GET ET SET    
    def get_solde(self):
        self.solde
    def set_solde(self,solde):
        self.solde
    #FONCTION DEPOT
    def depot (self,d):  
        self.solde+=d
        print("compte d'agence est crédité de      ",d," §")      
    #FONCTION COMMAND   
    def command(self,r):
        self.solde-=r
        print("le chef d'agence a fait un achat de ",r," §") 
        
c=Compte_agence(2000)
c.command(100)
c.depot(100)
print("solde restant de l'agence est de    ",c.solde," §")
