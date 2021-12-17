from graph import *
import numpy as np


#----------------------------------PARTIE 4.1------------------------------------#


def newBranch(G,s):
    V,E=G 
    V2=V.copy()
    E2=set()
    V2.remove(s)
    for e in E:
        if not s in e:
            E2.add(e)
    return V2,E2
def newBranchSet(G,ens):
    V,E=G 
    V2=V.copy()
    E2=set()
    for s in ens:
        V2.remove(s)
    for e in E:
        k=0
        for s in ens:
            if s in e:
                k=1
        if(k==0):
            E2.add(e)
    return V2,E2

def isLeaf(G):
    _,E=G
    return len(E) == 0

def branchAndBound(G):
    V,E = G
    C = set()
    bestVal = len(V)
    pile = []
    pile.append((V,E,C)) # On instancie la pile avec le graphe initial
    nbCoupe = 0
    nbFeuilles = 0
    nbNode = 0
    while len(pile)!=0:
        V,E,C = pile.pop() # On depile
        if isLeaf((V,E)) :
            nbFeuilles+=1
            if len(C) < bestVal :
                bestVal = len(C)
                bestCouverture = C
        else:
            nbNode+=1
            if len(C) < bestVal :
                # On récupère une nouvelle arete
                u_i,v_i = E.pop()

                # Branche 1
                C1 = C.copy()
                C1.add(u_i)
                V1,E1 = newBranch((V,E),u_i) # On creer les instances de la nouvelle branche a gauche
                pile.append((V1,E1,C1)) # on empile
                
                # Branche 2
                C2 = C.copy()
                C2.add(v_i)
                V2,E2 = newBranch((V,E),v_i) # On creer les instances de la nouvelle branche a droite
                pile.append((V2,E2,C2)) # on empile
            else:
                # Sinon on les resultats de  cette branche ne seront pas optimaux de toute façon,
                #donc on n'explore pas cette branche
                nbCoupe+=1
    return bestVal,bestCouverture,nbFeuilles,nbCoupe,nbNode


#----------------------------------PARTIE 4.2------------------------------------#
def addSetToSet(s1,s2):
    for e in s2:
        s1.add(e)
    return s1

def borneInferieure(graph,a):
    V,E=graph
    n=len(V)
    m=len(E)

    b1=int(m/GraphMaximalDegreeValue(graph))
    b2=len(a)/2
    b3=(2*n-1-np.sqrt((2*n-1)**2-8*m))/2
    return max(max(b1,b2),b3)


def solRealisAndBorneInf(graph):
    a=algo_couplage(graph)
    return (algo_couplage(graph),borneInferieure(graph,a))


def node(graph,v_ens,bestSol,nbNodeVisit):
    """ v contient les sommets qu'on veut mettre dans la couverture
    BestSol est la valeur de la meilleur solution trouvée.
    Par convention on prend BestSol={} au début"""
    
    V,E=graph 
    if(len(E)==0):
        """c'est une feuille, on renvoie la solution"""
        return (v_ens,nbNodeVisit)
    
    sol,borneInf=solRealisAndBorneInf(graph)
    borneInf+=len(v_ens)
    
    if(len(bestSol)==0):
        """bestSol n'est pas initialisé"""
        bestSol=sol
    elif(len(sol)+len(v_ens)<len(bestSol)):
        """on met à jour bestSol si on a trouvé une meilleure solution"""
        bestSol=addSetToSet(sol,v_ens)
      
    
    if(len(bestSol)<=borneInf or len(v_ens)>=len(bestSol)):
        """elagage"""
        return (bestSol,nbNodeVisit) 
    else:
        """on renvoie le noeud fils qui renvoie la couverture la plus petite"""
            
        edge=next(iter(E))
        e1,e2=edge
        
        v_ens1=v_ens.copy()
        v_ens1.add(e1)
        graph1=newBranch(graph, e1)
        res1,nbNodeVisit1=node(graph1,v_ens1,bestSol,nbNodeVisit+1)
        if(len(res1)<len(bestSol)):
            bestSol=res1
            
        v_ens2=v_ens.copy()
        v_ens2.add(e2)
        graph2=newBranch(graph, e2)
        res2,nbNodeVisit2=node(graph2,v_ens2,bestSol,nbNodeVisit1+1)
        
        if(len(res1)<len(res2)):
            return (res1,nbNodeVisit2)
        return (res2,nbNodeVisit2)
        
def BranchAndBoundBorns(graph):
    bestSol=set()
    v_ens=set()
    return node(graph,v_ens,bestSol,1)
def annexeNeighbors(graph,s):
    """on renvoie tous les sommets voisins de s"""
    V,E=graph
    res=set()
    for e in E:
        u,v=e
        if(u==s):
            res.add(v)
        elif(v==s):
            res.add(u)
    return res
    
def nodeImproved1(graph,v_ens,bestSol,nbNodeVisit):
    """ v contient les sommets qu'on veut mettre dans la couverture
    BestSol est la valeur de la meilleur solution trouvée.
    Par convention on prend BestSol={} au début"""
    
    V,E=graph 
    if(len(E)==0):
        """si c'est une feuille, on renvoie la solution"""
        return (v_ens,nbNodeVisit)
    
    sol,borneInf=solRealisAndBorneInf(graph)
    borneInf+=len(v_ens)
    
    if(len(bestSol)==0):
        """bestSol n'est pas initialisé"""
        bestSol=sol
    elif(len(sol)+len(v_ens)<len(bestSol)):
        """on met à jour bestSol si on a trouvé une meilleure solution"""
        bestSol=addSetToSet(sol,v_ens)
      
    
    if(len(bestSol)<=borneInf or len(v_ens)>=len(bestSol)):
        """elagage"""
        return (bestSol,nbNodeVisit) 
    
    else:
        """on renvoie le noeud fils qui renvoie la couverture la plus petite"""
            
        edge=next(iter(E))
        e1,e2=edge
        
        v_ens1=v_ens.copy()
        v_ens1.add(e1)
        graph1=newBranch(graph, e1)
        res1,nbNodeVisit1=nodeImproved1(graph1,v_ens1,bestSol,nbNodeVisit+1)
        if(len(res1)<len(bestSol)):
            bestSol=res1
            
        v_ens2=v_ens.copy()
        v_ens2.add(e2)
        graph2=newBranch(graph, e2)
        
        ens=annexeNeighbors(graph2,e1)
        v_ens2=addSetToSet(v_ens2,ens)
        
        v_ens2=v_ens.copy()
        v_ens2.add(e2)
        graph2=newBranch(graph, e2)
        
        ens=annexeNeighbors(graph2,e1)
        v_ens2=addSetToSet(v_ens2,ens)
        
        ens.add(e1)
        graph2=newBranchSet(graph2,ens)
        res2,nbNodeVisit2=nodeImproved1(graph2,v_ens2,bestSol,nbNodeVisit1+1)
        
        if(len(res1)<len(res2)):
            return (res1,nbNodeVisit2)
        return (res2,nbNodeVisit2)

def BranchAndBoundBornsImproved1(graph):
    bestSol=set()
    v_ens=set()
    return nodeImproved1(graph,v_ens,bestSol,1)

def nodeImproved2(graph,v_ens,bestSol,nbNodeVisit):
    """ v contient les sommets qu'on veut mettre dans la couverture
    BestSol est la valeur de la meilleur solution trouvée.
    Par convention on prend BestSol={} au début"""
    
    V,E=graph 
    if(len(E)==0):
        """c'est une feuille, on renvoie la solution"""
        return (v_ens,nbNodeVisit)
    
    sol,borneInf=solRealisAndBorneInf(graph)
    borneInf+=len(v_ens)
    
    if(len(bestSol)==0):
        """bestSol n'est pas initialisé"""
        bestSol=sol
    elif(len(sol)+len(v_ens)<len(bestSol)):
        """on met à jour bestSol si on a trouvé une meilleure solution"""
        bestSol=addSetToSet(sol,v_ens)
      
    
    if(len(bestSol)<=borneInf or len(v_ens)>=len(bestSol)):
        """elagage"""
        return (bestSol,nbNodeVisit) 
    else:
        """on renvoie le noeud fils qui renvoie la couverture la plus petite"""
            
        edge,_=GraphMaximalDegreeImproved(graph)
        e1,e2=edge
        
        v_ens1=v_ens.copy()
        v_ens1.add(e1)
        graph1=newBranch(graph, e1)
        res1,nbNodeVisit1=nodeImproved2(graph1,v_ens1,bestSol,nbNodeVisit+1)
        if(len(res1)<len(bestSol)):
            bestSol=res1
            
        v_ens2=v_ens.copy()
        v_ens2.add(e2)
        graph2=newBranch(graph, e2)
        
        ens=annexeNeighbors(graph2,e1)
        v_ens2=addSetToSet(v_ens2,ens)
        
        ens.add(e1)
        graph2=newBranchSet(graph2,ens)
        res2,nbNodeVisit2=nodeImproved2(graph2,v_ens2,bestSol,nbNodeVisit1+1)
        
        if(len(res1)<len(res2)):
            return (res1,nbNodeVisit2)
        return (res2,nbNodeVisit2)

def BranchAndBoundBornsImproved2(graph):
    bestSol=set()
    v_ens=set()
    return nodeImproved2(graph,v_ens,bestSol,1)

def nodeImprovedFac(graph,v_ens,bestSol,nbNodeVisit):
    """ v contient les sommets qu'on veut mettre dans la couverture
    BestSol est la valeur de la meilleur solution trouvée.
    Par convention on prend BestSol={} au début"""
    
    V,E=graph 
    if(len(E)==0):
        """c'est une feuille, on renvoie la solution"""
        return (v_ens,nbNodeVisit)
    
    sol,borneInf=solRealisAndBorneInf(graph)
    borneInf+=len(v_ens)
    
    if(len(bestSol)==0):
        """bestSol n'est pas initialisé"""
        bestSol=sol
    elif(len(sol)+len(v_ens)<len(bestSol)):
        """on met à jour bestSol si on a trouvé une meilleure solution"""
        bestSol=addSetToSet(sol,v_ens)
      
    
    if(len(bestSol)<=borneInf or len(v_ens)>=len(bestSol)):
        """elagage"""
        return (bestSol,nbNodeVisit) 
    else:
        """on renvoie le noeud fils qui renvoie la couverture la plus petite"""
            
        edge,degree=GraphMaximalDegreeImproved(graph)
        e1,e2=edge
        """e1 est le sommet de degré max"""
        degree=GraphDegree(graph)
        
        v_ens1=v_ens.copy()
        v_ens1.add(e1)
        graph1=newBranch(graph, e1)
        res1,nbNodeVisit1=nodeImprovedFac(graph1,v_ens1,bestSol,nbNodeVisit+1)
        if(len(res1)<len(bestSol)):
            bestSol=res1
            
        if(degree[e2]!=1):    
            v_ens2=v_ens.copy()
            v_ens2.add(e2)
            graph2=newBranch(graph, e2)
            
            ens=annexeNeighbors(graph2,e1)
            v_ens2=addSetToSet(v_ens2,ens)
            
            ens.add(e1)
            graph2=newBranchSet(graph2,ens)
            res2,nbNodeVisit2=nodeImprovedFac(graph2,v_ens2,bestSol,nbNodeVisit1+1)
        
            if(len(res1)<len(res2)):
                return (res1,nbNodeVisit2)
            return (res2,nbNodeVisit2)
        else:
            return (res1,nbNodeVisit1)

def BranchAndBoundBornsImprovedFac(graph):
    bestSol=set()
    v_ens=set()
    return nodeImprovedFac(graph,v_ens,bestSol,1)
