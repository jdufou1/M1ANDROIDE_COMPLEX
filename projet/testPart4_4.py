from graph import *
from graphPart4 import *
import numpy as np

"""
Ce test permet de répondre à la question 4.4 : Qualité des algorithmes approchés
rapport d'approximation : val(algo(I)) / OPT(I) <=> val(algo(I)) / algoBB(I)
"""



n = [i for i in range(10,100,5)]
p = 0.3


rapportGlouton = []
rapportCouplage = []


maxRapportCouplage = 0
valeurAlgoCouplage = 0

maxRapportGlouton = 0
valeurAlgoGlouton = 0

print(n)

for i in n:
    graph=GraphRandom(i,p)
    #print("i : ",i," p : ",p)
    V,E = graph
    V2 = V.copy()
    E2 = E.copy()
    start= time.time()
    solutionGlouton = algo_glouton((V2,E2))
    #print("solution glouton : ")
    #print(len(solutionGlouton))
    V2 = V.copy()
    E2 = E.copy()
    #print((V2,E2))
    solutionCouplage = algo_couplage((V2,E2))
    V2 = V.copy()
    E2 = E.copy()
    #print((V2,E2))
    opt,_ = BranchAndBoundBornsImproved1((V2,E2))
    end= time.time()
    rapportGlouton.append(len(solutionGlouton) / len(opt))
    rapportCouplage.append(len(solutionCouplage) / len(opt))
    # Verification du max pour glouton
    if (len(solutionGlouton) / len(opt)) > maxRapportGlouton:
        maxRapportGlouton = (len(solutionGlouton) / len(opt))
        valeurAlgoGlouton = solutionGlouton
    # Verification du max pour couplage
    if (len(solutionCouplage) / len(opt)) > maxRapportCouplage:
        maxRapportCouplage = (len(solutionCouplage) / len(opt))
        valeurAlgoCouplage = solutionCouplage
    print("Instance i = ", i," calculée en ",(end - start)," secondes")



print("rapport maximal d'approximation glouton = ",maxRapportGlouton," pour l'instance : ",valeurAlgoGlouton)
print("rapport maximal d'approximation couplage = ",maxRapportCouplage," pour l'instance : ",valeurAlgoCouplage)
"""
print("rapport glouton : ")
print(rapportGlouton)
print("rapport couplage : ")
print(rapportCouplage)
"""

pyplot.figure()
pyplot.plot(n,rapportCouplage,'red',label="algo couplage")
pyplot.plot(n,rapportGlouton,'blue',label="algo glouton")
pyplot.xlabel("taille du graphe n")
pyplot.ylabel("Rapport d'approximation avec la valeur optimale de l'instance")
pyplot.title("Taille des couvertures renvoyés par les 2 algos de la partie 3 avec p="+str(p))
pyplot.legend()
pyplot.show()








n = [i for i in range(10,100,5)]
p = 0.8


rapportGlouton = []
rapportCouplage = []


maxRapportCouplage = 0
valeurAlgoCouplage = 0

maxRapportGlouton = 0
valeurAlgoGlouton = 0

for i in n:
    graph=GraphRandom(i,p)
    #print("i : ",i," p : ",p)
    V,E = graph
    V2 = V.copy()
    E2 = E.copy()
    start= time.time()
    solutionGlouton = algo_glouton((V2,E2))
    #print("solution glouton : ")
    #print(len(solutionGlouton))
    V2 = V.copy()
    E2 = E.copy()
    #print((V2,E2))
    solutionCouplage = algo_couplage((V2,E2))
    V2 = V.copy()
    E2 = E.copy()
    #print((V2,E2))
    opt,_ = BranchAndBoundBornsImproved1((V2,E2))
    end= time.time()
    rapportGlouton.append(len(solutionGlouton) / len(opt))
    rapportCouplage.append(len(solutionCouplage) / len(opt))
    # Verification du max pour glouton
    if (len(solutionGlouton) / len(opt)) > maxRapportGlouton:
        maxRapportGlouton = (len(solutionGlouton) / len(opt))
        valeurAlgoGlouton = solutionGlouton
    # Verification du max pour couplage
    if (len(solutionCouplage) / len(opt)) > maxRapportCouplage:
        maxRapportCouplage = (len(solutionCouplage) / len(opt))
        valeurAlgoCouplage = solutionCouplage
    print("Instance i = ", i," calculée en ",(end - start)," secondes")



print("rapport maximal d'approximation glouton = ",maxRapportGlouton," pour l'instance : ",valeurAlgoGlouton)
print("rapport maximal d'approximation couplage = ",maxRapportCouplage," pour l'instance : ",valeurAlgoCouplage)
"""
print("rapport glouton : ")
print(rapportGlouton)
print("rapport couplage : ")
print(rapportCouplage)
"""


pyplot.figure()
pyplot.plot(n,rapportCouplage,'red',label="algo couplage")
pyplot.plot(n,rapportGlouton,'blue',label="algo glouton")
pyplot.xlabel("taille du graphe n")
pyplot.ylabel("Rapport d'approximation avec la valeur optimale de l'instance")
pyplot.title("Taille des couvertures renvoyés par les 2 algos de la partie 3 avec p="+str(p))
pyplot.legend()
pyplot.show()