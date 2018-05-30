from BloomFilter import BloomFilter
class OccurenceBloom:
	def __init__(self):
		self.tableau=[]
		self.filtre=BloomFilter(600,2)
		self.faux_positive=0
	def ajouter(self,adresse):
		if(self.filtre.existe(adresse)):
			existe=False
			taille=len(self.tableau)
			for i in range(taille):
				if(self.tableau[i][0]==adresse):
					existe=True
					self.tableau[i]=(adresse,self.tableau[i][1]+1)
					self.faux_positive+=1				
					break
			if not existe:
				self.tableau.append((adresse,1))
		else:
			self.tableau.append((adresse,1))
		self.filtre.ajouter(adresse)

		


