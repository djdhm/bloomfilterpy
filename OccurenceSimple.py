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
				break
		if not existe:
			self.tableau.append((adresse,1))

		

	



	
