"""Un graphe sera représenté par le tuple (set(int),set(int*int)) où set(int)
est l'ensemble des sommets et set(int*int) est l'ensemble des arêtes"""

import os,random
import time
import csv

from matplotlib import pyplot

def graphCreate(nameFile):
        """string -> (set(int),set(int*int))
        nameFile est le nom du fichier txt qui contient les informations du graphe.
        On crée la variable graph qui contient un tuple (V,E) caractérisant le graphe"""
        graphText=open(nameFile,"r")
        lines=graphText.readlines()
        vertex=set()
        edges=set()
        nb_vertex=int(lines[1][:-1])
        nb_edges=int(lines[4+nb_vertex][:-1])
        for i in range(nb_vertex):
            vertex.add(int(lines[3+i][:-1]))
        for i in range(nb_edges):
            tmp=lines[6+nb_vertex+i][:-1].split(' ')
            edges.add((int(tmp[0]),int(tmp[1])))
        return (vertex,edges)

def deleteVertex(graph,v):
    """(set(int),set(int*int))*int -> (set(int),set(int*int))
    Question 2.1.1 cette fonction renvoie un graphe sans le sommet v
    graph est le graphe et v est le sommet à supprimer"""
    vertex,edges=graph
    if(not v in vertex):
        return graph
    
    vertex2=vertex.copy()
    vertex2.remove(v)
    edges2=set()
    for e in edges:
       if not v in e:
           edges2.add(e)
    return (vertex2,edges2) 

def deleteMultipleVertex(graph,ev) :
    """(set(int),set(int*int))*list(int) -> (set(int),set(int*int))
    Question 2.1.2 cette fonction renvoie un graphe sans les sommet de ev
    graph est le graphe et ev est la liste des sommets à supprimer"""
    vertex,edges=graph
    graph2=graph
    for v in ev:
        graph2=deleteVertex(graph2,v)
    return graph2

def GraphDegree(graph):
    """(set(int),set(int*int)) -> dict(int:int)
    Question 2.1.3, on renvoie les degré des sommets du graphe, les degrés sont renvoyés
    sous forme de dictionnaire ou la clé est l'identifiant du sommet et la valeur est son degré """
    vertex,edges=graph
    res={}
    for v in vertex:
        cpt=0
        for e in edges:
            if v in e:
                cpt+=1
        res[v]=cpt
    return res

def GraphMaximalDegree(graph):
    """(set(int),set(int*int)) -> int
    Question 2.1.3, on renvoie le sommet de degré max"""
    dictdeg=GraphDegree(graph)
    vertmax = max(dictdeg, key=dictdeg.get)
    return vertmax

def GraphMaximalDegreeImproved(graph):
    """(set(int),set(int*int)) -> int,dict(int:int)
    Question 2.1.3, on renvoie une arête dont une des extrémités est le sommet 
    de degré max ainsi que l'ensemble des degrés"""
    V,E=graph
    dictdeg=GraphDegree(graph)
    vertmax = max(dictdeg, key=dictdeg.get)
    for e in E:
        u,v=e
        if(u==vertmax):
            return (e,dictdeg)
    return (next(iter(E)),dictdeg)

def GraphMaximalDegreeValue(graph):
    """(set(int),set(int*int)) -> int

    on renvoie le degré max"""
    dictdeg=GraphDegree(graph)
    vertmax = max(dictdeg, key=dictdeg.get)
    return dictdeg[vertmax]


def GraphRandom(n,p):
    """int*float->(set(int),set(int*int)) 
    Question 2.2.1 on crée un un graphe de manière aléatoire"""
    vertex={i for i in range(n)}
    listvertex=list(vertex)
    edges=set()
    for i in vertex:
        for j in listvertex:
            if(i!=j and (not (i,j) in edges) and (not (j,i) in edges)):
                if(random.random()<p):
                    edges.add((i,j))
        """ on ne veut pas qu'une même arête soit testée deux fois, donc on enlève v des sommets
        de listvertex, ainsi (i,j) et (j,i) ne seront pas testés toutes les deux 
        mais soit (i,j) soit (j,i)"""
        listvertex.remove(i)
    return (vertex,edges)

"""
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
"""    


def algo_couplage(graph):
    _,edges=graph
    C = set()
    for edge in edges: # On parcours les arretes
        isInside = False # Drapeau qui permet de savoir si l'arrete est dans C ou non
        for vtx in edge: # On analyse les sommets de l'arrete
            for vtxC in C: # Ici on va vérifier les conditions sur C
                if vtxC == vtx:
                    isInside = True
        if not isInside :
            for e in edge:
                C.add(e)
    return C

def algo_glouton(graph):
    _,E=graph
    C = set()
    while len(E) != 0 :
        v = GraphMaximalDegree(graph)
        C.add(v)
        toRemove = set()
        for e in E:
            for vertex in e:
                if v == vertex:
                    toRemove.add(e)
        for e in toRemove:
            E.remove(e)
    return C


def isCouplage(couplage , graph):
    _,E=graph
    toCheck = set() # ensemble qui va contenir toutes les arêtes engendrées par notre couplage dans le graphe
    for v_couplage in couplage:
        for edge in E:
            if v_couplage in edge: # Si un sommet de notre couplage \in edge alors peut ajouter l'arrete engendré par ce sommet dans l'ensemble a verifier
                if not edge in toCheck: # On ajoute pas deux fois la meme arrete dans l'ensemble
                    toCheck.add(edge)
    return toCheck == E

def isCouverture(ens , graph):
    _,E=graph
    toCheck = set() # ensemble qui va contenir toutes les arêtes engendrées par notre couplage dans le graphe
    for edge in E:
        k=0
        for v in ens:
            if(v in edge):
                k=1
        if(k==0):
            return False
    return True

