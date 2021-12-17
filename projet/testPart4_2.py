from graph import *
from graphPart4 import *
import numpy as np
from math import log
from sys import exit

timeNoBorne=[]
timeBorne=[]
nbNoeudsBornes=[]
nbNoeudsNoBornes=[]
N=[i for i in range(2,22,2)]
p=0.5
for i in N:
    t=5
    branchBornes=0
    branchNoBornes=0
    for _ in range(t):
        graph=GraphRandom(i,p)
        print(graph)
        print("--------------- "+str(i)+"----------------")
        
        start1 = time.time()
        couvBorne1,nbn=BranchAndBoundBorns(graph)
        end1 = time.time()
        timeBorne.append(end1-start1)
        branchBornes+=(end1-start1)
        
        start2 = time.time()
        BandBVal,couvBorne2,nbFeuilles,nbCoupe,nbNode = branchAndBound(graph)
        end2 = time.time()
        timeNoBorne.append(end2-start2)
        branchNoBornes+=(end2-start2)
        
        if (isCouverture(couvBorne1,graph) and len(couvBorne2)==len(couvBorne1)):
            print("solution valide")
        else:
            print("Solution non valide")
            print(couvBorne1,couvBorne2)
            exit(0)
    nbNoeudsBornes.append(branchBornes/t)
    nbNoeudsNoBornes.append(branchNoBornes/t)


pyplot.figure()
pyplot.plot(N,nbNoeudsNoBornes,'red',label="sans bornes")
pyplot.plot(N,nbNoeudsBornes,'blue',label="avec bornes")
pyplot.xlabel("Taille de l'instance n")
pyplot.ylabel("Temps en secondes ")
pyplot.title("Temps de calcul des algos BranchAndBound avec p="+str(p))
pyplot.legend()
pyplot.show()
