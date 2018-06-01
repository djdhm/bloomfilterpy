class OccurenceSimple:
	def __init__(self):
		self.tableau=[]

	def ajouter(self,adresse):
		existe=False
		taille=len(self.tableau)
		for i in range(taille):
			if(self.tableau[i][0]==adresse):
				existe=True
				self.tableau[i]=(adresse,self.tableau[i][1]+1)
		if not existe:
			self.tableau.append((adresse,1))

		
	def dix_premier(self):
		return sorted(self.tableau,key=lambda x:-x[1])[0:10]

	
	def reset(self):
		self.tableau=[]


	
