from PIL import Image as im
import random 
import numpy as np
from matplotlib import pyplot as plt
file="image/lena512.gif"
#Chargement de l’image par PIL et affichage des propriétés de l’image
try:
    photo = im.open(file)
    print ("Propriétés image : ")
    print (file , photo.format , "%dx%d" %photo.size , photo.mode)
except IOError :
    print (" Erreur lors de l’ouverture du fichier !")
#get data donne une liste lisible par PIL uniquement
pixels =list(photo.getdata())
#np.array( ) permet d’obtenir une matrice du type array de numpy :
tableauPixels =np.array(photo)
#afficher le nombre des éléments de la matriche
print(np.size(tableauPixels))
#afficher les dimentions
print(np.shape(tableauPixels))
# on fait une copie du tableau initial pour garder la matrice originale :
M=np.copy(tableauPixels)
# print(tableauPixels)
# rouge = M[:,:,0]
# vert = M[:,:,1]
# bleu = M[:,:,2]

# histogram, bin_edges = np.histogram(rouge,bins=256, range=(0, 255))
# histogram1, bin_edges = np.histogram(vert,bins=256, range=(0, 255))
# histogram2, bin_edges = np.histogram(bleu,bins=256, range=(0, 255))
# fig = plt.figure(figsize=(12, 6))
# plt.title("Histogram")
# plt.xlabel("niveau de gris")
# plt.ylabel("nombre de pixel")
# plt.xlim([0.0, 255.0])
# plt.grid()
# plt.plot(bin_edges[0:-1], histogram)
# plt.plot(bin_edges[0:-1], histogram2)
# plt.plot(bin_edges[0:-1], histogram1)
# plt.show()
#exportation en png : très rapide et ne plante pas la console
i=0
def export(matrice):
    nouvellePhoto =im.fromarray(matrice)
    nouvellePhoto.save("image/image_mod{}.png".format(random.randint(1,255)), "PNG")
    
# export(M)

# def seuillage(ima):
#     resultat = np.copy(ima)
#     s = np.shape(resultat)
#     for j in range(s[0]):
#         for i in range(s[1]):
#             # print(resultat[50,40,1])
#             resultat[j,i,0] = 0
#             resultat[j,i,2] = 0

#     return resultat
# def modifier(ima):
#     pi = 0.5
#     p = np.copy(ima)
#     s = np.shape(p)
#     for j in range(s[0]):
#         for i in range(s[1]):
#             p[j, i, 1]=0
#             p[j, i, 2]=0
#             p[j , i ,0]=p[j, i,0]*pi
#             if p[j, i, 0]<0:
#                 p[j, i, 0]=0
#     return p
# T = modifierLena(M)
def modifierLena(ima):
    pi = -1
    l= []
    p = np.copy(ima)
    s = np.shape(p)
    print(len(p))
    print(len(p[0]))
    for j in range(1,len(p)-1):
        for i in range(s[1]):
            l.append(p[j-1 ,i-1])
            p[j , i]=(p[j, i]*pi)+255
            # if p[j, i]<0:
            #     p[j, i]=0
    return p
T = modifierLena(M)
# export(T)
# T=seuillage(M)
# nouvellePhoto =im.fromarray(T)
# nouvellePhoto.save("image/imag.jpeg", "JPEG")