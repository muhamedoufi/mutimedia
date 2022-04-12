from PIL import Image as im
import matplotlib.pyplot as plt
import numpy as np
# stocker le lien dans un variable file
file="image/img1.jpeg"
#Chargement de l’image par PIL et affichage des propriétés de l’image
# ajoutre try except pour gerer les exceptions
try:
    # charger l'image et le stocker dans la variable photo
    photo = im.open(file)
    # afficher les proprietes de l'image
    print ("Propriétés image : ")
    print (file , photo.format , "%dx%d" %photo.size , photo.mode)
except IOError :
    print (" Erreur lors de l’ouverture du fichier !")
#get data donne une liste lisible par PIL uniquement
pixels =list(photo.getdata())
# print("getdata result : ",pixels)

#np.array( ) permet d’obtenir une matrice du type array de numpy :
tableauPixels =np.array(photo)
# print("tableauPixels : ",tableauPixels)
#afficher le nombre des éléments de matrice ou bien size
print(np.size(tableauPixels))
#afficher les dimentions
print(np.shape(tableauPixels))
# on fait une copie du tableau initial pour garder la matrice originale :
M=np.copy(tableauPixels)
print("matrice tableauPixels : ",tableauPixels)
print("matrice M : ",M)
#exportation en png : très rapide et ne plante pas la console
def export (matrice):
    nouvellePhoto =im.fromarray(matrice)
    nouvellePhoto.save("image/image.png", "PNG")
# pour exporter le tableau de Pixels en image
export(M)

def seuillage(ima,seuil):
    resultat = np.copy(ima)
     # pour recuperer la dimention
    s = np.shape(resultat)
    for j in range(s[0]):
        for i in range(s[1]):
            # print(resultat[50,40,1])
            if resultat[j,i,1] > seuil:
               resultat[j,i,1] = 1
            else:
                resultat[j,i,1] = 0
    return resultat

T=seuillage(M,240)