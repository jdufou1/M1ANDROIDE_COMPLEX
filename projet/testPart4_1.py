from graph import *
from graphPart4 import *
import numpy as np
from math import log


p=0.3
timeTree=[]
N=[i for i in range(2,23)]
for n in N:
    t=5
    s=0
    for i in range(t):
        graph=GraphRandom(n,p)
        
        #print("--------------------------")
        #print("ALGORITHME BRANCH AND BOUND")
        start_branchAndBound = time.time()
        BandBVal,BandBCouverture,nbFeuilles,nbCoupe,nbNode = branchAndBound(graph)
        end_branchAndBound = time.time()
        s+=(end_branchAndBound - start_branchAndBound)
        #print("Taille de la réponse de l'algo couplage = ",BandBVal)
        #print("Taille de la réponse de l'algo branchAndBound = ",len(BandBCouverture))
        
        #print("Temps algo Branch And Bound : ",round((end_branchAndBound - start_branchAndBound),4),"s")
        #print("Stats:")
        print("Nombre de noeuds évalues = ",nbNode)
        #print("Nombre de feuilles évaluées : ",nbFeuilles)
        #print("Nombre d'élagages de l'arbre : ",nbCoupe)
        # Vérification de la réponse de l'algo :
        if isCouverture(BandBCouverture,graph):
            print("Solution de l'algo Branch and Bound est valide.")
            print(BandBCouverture)
        else:
            print("Solution de l'algo Branch and Bound est non valide.")
        print("\n")
    timeTree.append(log(s/t))
pyplot.figure()
pyplot.plot(N,timeTree,'red')
pyplot.xlabel("log Taille de l'instance log(n)")
pyplot.ylabel("Temps en seconde (s) ")
pyplot.title("Nb de noeuds visitées pour p="+str(p)+" en fct du log de la taille de l'entrée")
pyplot.show()