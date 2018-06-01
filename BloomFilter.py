from TableauBit import TableauBit
import murmurpy as bibhash
class BloomFilter:
    
    def __init__(self, taille, nb_fct):
        self.taille = taille
        self.nb_fcthash = nb_fct
        self.tab_bit = TableauBit(taille)
        
    def ajouter(self, adresse):
        #Mise a 1 des indices donnes par les fonctions de hashage
        for i in xrange(self.nb_fcthash):
            x=bibhash.hash64(adresse,i)
            self.tab_bit.ajouter(x%self.taille)

	
    def existe(self, adresse):
        #Verifier l'existence de l'element grace au fct de hashge 
        for cpt in xrange(self.nb_fcthash):
            indice=bibhash.hash64(adresse,cpt)
            if(not self.tab_bit.existe(indice%self.taille)):
                return False	
        return True
	
    def hash(self, adresse):
	prop=[]
	sub=""
	for x in adresse:
		if(x=="."):
			prop.push(chaine%self.taille)
		else:
			chaine+=x
		
