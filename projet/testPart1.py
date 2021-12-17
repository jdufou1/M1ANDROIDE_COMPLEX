from graph import *

#TESTS PARTIE 1
graph=graphCreate('exempleinstance.txt')  
print(graph)
print("----------------------")
#on effectue les tests sur des graphes de différentes tailles
for i in range(2,10,2):
    graph=GraphRandom(i,0.5)
    print(graph)
    print(GraphMaximalDegree(graph))
    graph=deleteMultipleVertex(graph,[0,1])
    print(graph)
    print("----------------------")

