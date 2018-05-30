

from OccurenceSimple import OccurenceSimple 
from OccurenceBloom import OccurenceBloom
import time
import csv 





simple=OccurenceSimple()
print("demarrer le comptage avec recherche filtre bloom ")
temps_debut = time.clock()
d=1
#Premiere Demarche : Ajout avec recherche simple 
with open('log20170630.csv', 'rb') as fichier:
     reader = csv.reader(fichier, delimiter=',')
     for ligne in reader:
	 d+=1
         simple.ajouter(ligne[0])
	 if(d==50000):
		 break

temps_fin = time.clock()
print("temps d execution  est ",temps_fin-temps_debut)




#Deuxieme Demarche : Ajout avec filtre Bloom 
bloom = OccurenceBloom()

print("demarrer le comptage avec recherche simple")
print("........................................")
temps_debut = time.clock()
d=1
#Premiere Demarche : Ajout avec recherche simple 
with open('log20170630.csv', 'rb') as fichier:
     reader = csv.reader(fichier, delimiter=',')
     for ligne in reader:
	 d+=1
         bloom.ajouter(ligne[0])
	 if(d==50000):
		 break

temps_fin = time.clock()
print("le nombre de faux positif est:",bloom.faux_positive)
print("temps d execution  est ",temps_fin-temps_debut)
print("adresse     Frequence ")
for test in bloom.tableau:
	print(test[0]  ," == ",test[1])
