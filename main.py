

from OccurenceSimple import OccurenceSimple 
from OccurenceBloom import OccurenceBloom
import time
import csv 
import os


def changer_ligne(nombre):
	global lignes
	lignes=nombre
def changer_data(nom_fichier):
	global data
	data=nom_fichier

def exec_choix(numero):
	if(numero==1):
		d=1
		#Premiere Demarche : Ajout avec recherche simple 
		temps_debut = time.clock()
		print("demarrer le comptage avec recherche simple")
		print("........................................")

		with open(data, 'rb') as fichier:
		     reader = csv.reader(fichier, delimiter=',')
		     for ligne in reader:
			 d=d+1
			 simple.ajouter(ligne[0])
			 if(d==lignes):
				break
		temps_fin = time.clock()
		print("temps d execution  est ",temps_fin-temps_debut)
		top_dix=simple.dix_premier()
		print "La liste des top 10"
		for top in top_dix:
			print top[0]," === " ,top[1]
		
		bloom.sauvegarder()
	if(numero==2):
		print(lignes)
		print(bloom.taille)
		print(bloom.nb_function)
		#Deuxieme Demarche : Ajout avec filtre Bloom 
		print("demarrer le comptage avec recherche bloom")
		print("........................................")
		temps_debut = time.clock()
		d=1

		with open(data, 'rb') as fichier:
		     reader = csv.reader(fichier, delimiter=',')
		     for ligne in reader:
			 d+=1
			 bloom.ajouter(ligne[0])
			 if(d==lignes):
				break

		temps_fin = time.clock()
		print("le nombre de faux positif est:",bloom.faux_positive)
		print("le Taux d'erreur est : ",bloom.faux_positive*1.0/lignes)
		print("temps d execution  est ",temps_fin-temps_debut)
		#Extraire les dix plus frequents	
		top_dix=bloom.dix_premier()
		print "La liste des top 10"
		for top in top_dix:
			print top[0]," === " ,top[1]
		
		bloom.sauvegarder()


	if(numero==5):
		with open(data, 'rb') as fichier:
		     cpt=0
		     for ligne in fichier:
			 cpt+=1
		print("le nombre de lignes est ",cpt)
		 	
	if(numero==3):
		print("lancer une comparaison entre les deux methodes : ")
		d=1
		#Premiere Demarche : Ajout avec recherche simple 
		temps_debut = time.clock()
		print("demarrer le comptage avec recherche simple")
		print("........................................")

		with open(data, 'rb') as fichier:
		     reader = csv.reader(fichier, delimiter=',')
		     for ligne in reader:
			 d=d+1
			 simple.ajouter(ligne[0])
			 if(d==lignes):
				break
		temps_fin = time.clock()
		temps_simple=temps_fin-temps_debut
		
		d=1
		#Premiere Demarche : Ajout avec recherche simple 
		temps_debut = time.clock()
		print("demarrer le comptage avec recherche filtre bloom")
		print("........................................")

		with open(data, 'rb') as fichier:
		     reader = csv.reader(fichier, delimiter=',')
		     for ligne in reader:
			 d=d+1
			 bloom.ajouter(ligne[0])
			 if(d==lignes):
				break
		temps_fin = time.clock()
		temps_bloom=temps_fin-temps_debut
		print("temps d'execution avec R.simple = ",temps_simple)
		print("temps d'execution avec R.avec filtre  = ",temps_bloom)
		if(temps_bloom<temps_simple):
			print("le filtre est efficace pour ",lignes,"lignes")
		else:
			print("le filtre n'est pas efficace pour",lignes,"lignes ")
	if(numero==8):
		num=input("entrez le nombre de lignes que vous voulez lire : ")	
		changer_ligne(num)
	if(numero==6):
		num=input("saisissez la nouvelle taille de filtre : ")
		bloom.changer_taille(num)

	
	if(numero==7):
		num=input("saisissez le nombre de fonctions de hachage : ")
		bloom.changer_nb_fct(num)
	bloom.reset()
	simple.reset()	
	raw_input("appuyez sur une touche pour continuer...")
	
#	if(numero==4):
#		data=input("entrez le nom de nouveau fichier")
def menu():
	os.system('clear')  	  
	print "Bienvenue,\n"
	print "Veuillez faire un choix pour commencer :"
	print "1. Effectuer le comptage sans filtre Bloom"
	print "2. Effectuer le comptage avec filtre Bloom "
	print "3. Comparer les deux methodes  "
	print "4. Changer le nom de fichier "
	print "5. Compter le nombre de lignes dans le fichier "
	print "6. Changer la taille de filtre "
	print "7. Changer le nombre de fonctions de Hachage"
	print "8. Changer le nombre de lignes a lire  "
	print "\n0. Quitter"


simple=OccurenceSimple()

changer_data('log20170630.csv')
print("demarrer le comptage avec recherche simple ")
bloom = OccurenceBloom()
changer_ligne(2000)  # nombre de ligne a lire depuis le fichier
choix=-1
while(choix!=0):
	menu()
	choix = input(" >>  ")
	exec_choix(choix)


print("au revoir ")


