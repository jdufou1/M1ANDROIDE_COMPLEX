from graph import *
from math import log

graph2=GraphRandom(6,0.5)
print(graph2)

print(algo_couplage(graph2))
print(algo_glouton(graph2))

if isCouverture(algo_couplage(graph2),graph2):
    print("Algo fonctionne avec algo_couplage")

if isCouverture(algo_glouton(graph2),graph2):
    print("Algo fonctionne avec algo_glouton")


# Tests des algos

n = [i for i in range(2,153,30)]
p = 0.5


couplage_gn = []
glouton_gn = []
isValide_couplage = []
isValide_glouton = []
timeCouplage = []
timeGlouton = []

# Test sur l'algo couplage
for i in n:
    graph=GraphRandom(i,p)
    #print("[Test] : n = ",i,", p = ",p)
    #print("--------------------------")
    s=0
    s2=0
    tn=5
    for j in range(tn):
        start= time.time()
        couv1 = algo_couplage(graph)
        couplage_gn.append(len(couv1))
        end = time.time()
        
        start2= time.time()
        couv2 = algo_glouton(graph)
        glouton_gn.append(len(couv2))
        end2 = time.time()
        
        # Vérification de la réponse de l'algo :
        if isCouverture(couv1,graph):
            print("Solution de l'algo couplage est valide.")
            isValide_couplage.append(1)
        else:
            print("Solution de l'algo couplage est non valide.")
            isValide_couplage.append(0)
            
        if isCouverture(couv1,graph):
            print("Solution de l'algo glouton est valide.")
            isValide_glouton.append(1)
        else:
            print("Solution de l'algo glouton est non valide.")
            isValide_glouton.append(0)
          
        s+=len(couv1)
        s2+=len(couv2)
        #s+=(end - start)/tn
        #s2+=(end2 - start2)/tn
    timeCouplage.append(s/tn)
    timeGlouton.append(s2/tn)
    #timeCouplage.append(log(s))
    #timeGlouton.append(log(s2))
    print("\n")


# Enregistrement du test dans un fichier csv de la forme : 
#   tailleInstance = n | proba = b | taille(algo_couplage(graphe(n,p))) | temps de algo_couplage(graphe(n,p)) |validite de algo_couplage(graphe(n,p)) 
#                                  | taille(algo_glouton(graphe(n,p))) | temps de algo_glouton(graphe(n,p)) |validite de algo_glouton(graphe(n,p)) 
with open('dataSetGraphCouplage.csv', 'w') as file:
    filewriter = csv.writer(file, delimiter=',',quotechar='|',)
    filewriter.writerow(["n","p","len(couplage(G(n,p)))","time(couplage(G(n,p)))","isValid(couplage(G(n,p)))","len(glouton(G(n,p)))","time(glouton(G(n,p)))","isValid(glouton(G(n,p)))"])
    for i in range(len(n)):
        value = [n[i],p,couplage_gn[i],timeCouplage[i],isValide_couplage[i],glouton_gn[i],timeGlouton[i],isValide_glouton[i]]
        filewriter.writerow(value)

pyplot.figure()
pyplot.plot(n,timeCouplage,'red',label="algo couplage")
pyplot.plot(n,timeGlouton,'blue',label="algo glouton")
pyplot.xlabel("taille du graphe n")
pyplot.ylabel("taille de la couverture renvoyée ")
pyplot.title("Taille des couvertures renvoyés par les 2 algos de la partie 3 avec p="+str(p))
pyplot.legend()
pyplot.show()

