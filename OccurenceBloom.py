import pickle
from BloomFilter import BloomFilter
class OccurenceBloom:
	def __init__(self):
		#Initialisation de filtre avec une taille de 1200 bits 
		#et deux fonctions de hashage 
		self.tableau=[]
		self.nb_function=1
		self.taille=33000
		self.filtre=BloomFilter(300,2)
		self.faux_positive=0
		self.res="resultBloom.csv"
	def ajouter(self,adresse):
		#Verifier si le hash de l adresse existe dans le filtre 
		if(self.filtre.existe(adresse)):
			#Si oui , on verifie si ce n'est pas un faux positive			
			existe=False
			taille=len(self.tableau)
			#Recherche normal dans le tableau de frequence 	
			for i in range(taille):
				if(self.tableau[i][0]==adresse):
					existe=True
					self.tableau[i]=(adresse,self.tableau[i][1]+1)
					break
			if not existe:
			#Un faux positive detecte, on insere la nouvelle adresse
				self.tableau.append((adresse,1))
				self.faux_positive+=1				
		else:
		#Le hash n existe pas on insere directement a la fin 
			self.tableau.append((adresse,1))
		#On mets a jour le filtre 	
		self.filtre.ajouter(adresse)
	
	def sauvegarder(self):
		with open("save.bloom","wb") as sauvegarde:
			pickle.dump(self, sauvegarde, pickle.HIGHEST_PROTOCOL)			
		print("sauvegarde en cours ....")

	def reset(self):
		self.tableau=[]
		self.filtre=BloomFilter(self.taille,self.nb_function)
		self.faux_positive=0
	def dix_premier(self):
		return sorted(self.tableau,key=lambda x:-x[1])[0:10]

	def changer_taille(self,taille):
		self.taille=taille
		self.filtre=BloomFilter(taille,self.nb_function)
		
	def changer_nb_fct(self,nb_function):
		self.nb_function=nb_function
		self.filtre=BloomFilter(self.taille,nb_function)	
