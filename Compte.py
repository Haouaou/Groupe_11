# HAOUAou DALI 18A847FS

class Compte: #création classe mère Compte bancaire
    
    """Classe représentant le compte d'une personne"""
    def __init__(self,n = 0,solde = 0.0):
        self._numero = n
        self._solde = solde
        
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        
        return "Code compte : {0} \nSolde : {1}\n".format(self._numero, self.solde)
    
    def _get_numero(self):
        print("Votre numéro de compte est : {0} \n".format(self._numero))
        return self._numero
    
    def _get_solde(self):
        print("Votre solde est de {0} FCFA \n".format(self._numero))
    
    def _set_solde(self,new_solde):
        print("Votre nouveau solde est de {0} FCFA \n".format(new_solde))
        self._solde = new_solde
    
    def infoSolde(self):
        print("Votre solde est de {0} FCFA ! \n".format(self._solde))

    def versement(self,add):
        self._solde += add
        print("Versement de {0} FCFA éffectué ! \n".format(add))
        self.infoSolde()
    
    def retrait(self,moins):
        self._solde -= moins
        print("Le montant débité est de {0} FCFA\n".format(moins))
        self.infoSolde()
    
    solde = property(_get_solde, _set_solde)    
    numero = property(_get_numero)
