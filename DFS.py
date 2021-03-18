from Graphe import graphe
from collections import deque

#faites des recherche sur la bebliotheque deque sur youtube ;)

class DFS():
    # constructeur de la classe BFS
    def __init__(self, graphe):
        self.graphe = graphe

    def rechercherDFS(self, graphe, start, goal):
            avisite = deque() # la liste des noeuds à visiter
            avisite.append(start)
            visite = []  # la liste noeud déja visité
            while avisite:
                i = avisite.popleft()
                if i not in visite:

                    visite.append(i)
                    avisite.extendleft(graphe[i])  # sucesseurs de n

                    if i == goal:
                        break
            return visite

# dfs = DFS(graphe)
# print(dfs.rechercherDFS(graphe, 'A', 'F'))

