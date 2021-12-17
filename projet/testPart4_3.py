from graph import *
from graphPart4 import *
import numpy as np
from math import log
from sys import exit


x1=[]
x2=[]
x3=[]
x4=[]
N=[i for i in range(2,25,3)]
p=0.3
t=10
for i in N:
    l1=0
    l2=0
    l3=0
    l4=0
    branchNoBornes=0
    for _ in range(t):
        graph=GraphRandom(i,p)
        print(graph)
        print("--------------- "+str(i)+"----------------")
        
        start1 = time.time()
        couvBorne1,nbn1=BranchAndBoundBornsImproved2(graph)
        end1 = time.time()
        #l1+=(end1-start1)
        l1+=nbn1
        
        """
        start2 = time.time()
        couvBorne2,nbn2=BranchAndBoundBorns(graph)
        end2 = time.time()
        #l2+=log(end2-start2)
        l2+=log(nbn2)
        """
        
        start3 = time.time()
        couvBorne3,nbn3=BranchAndBoundBornsImproved1(graph)
        end3 = time.time()
        #l3+=(end3-start3)
        l3+=nbn3
        
        start4 = time.time()
        couvBorne4,nbn4=BranchAndBoundBornsImprovedFac(graph)
        end4 = time.time()
        #l4+=(end4-start4)
        l4+=nbn4
        
        if (isCouverture(couvBorne3,graph) and len(couvBorne4)==len(couvBorne1)):
            print("solution valide")
        else:
            print("Solution non valide")
            print(couvBorne4,couvBorne1)
            exit(0)
    x1.append(l1/t)
    #x2.append(l2/t)
    x3.append(l3/t)
    x4.append(l4/t)


pyplot.figure()
#pyplot.plot(N,x2,'red',label="branchement non amelioré mais borné")
pyplot.plot(N,x3,'purple',label="branchement amelioré n°1")
pyplot.plot(N,x1,'blue',label="branchement amelioré n°2")
pyplot.plot(N,x4,'green',label="branchement amelioré fac")


pyplot.xlabel("Taille n du graphe")
pyplot.ylabel("Nombre de noeuds visités ")
pyplot.title("Nombre de noeuds visités avec les algos BranchAndBound des Q 4.3.1, 4.3.2, 4.3.3  avec p="+str(p))
pyplot.legend()
pyplot.show()
