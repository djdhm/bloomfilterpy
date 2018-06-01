from struct import *
class TableauBit:

    def __init__(self,taille):
	initial,=unpack("B",'\x00')
        self.taille=taille
        self.tableau=[initial]*((taille//8)+1)



    def existe(self,indice):
        numCase=indice//8
	numBit=indice % 8
	bit=self.tableau[numCase]
	test=(bit>>numBit) & 1
	return test	

    def ajouter(self,indice):
	numCase=indice//8
	numBit=indice % 8
	self.tableau[numCase]=self.tableau[numCase]|(1<<numBit)

