from Graphe import graphe
from collections import deque

# essayes de documenter sur la lib deque et ces fonction qu'on a utilisé ici sur ce lien :  https://docs.python.org/2.5/lib/deque-objects.html

class BFS():
    # constructeur de la classe BFS
    def __init__(self, graphe):
        self.graphe = graphe

    # fonction de recherche en bfs
    def rechercherBFS(self, graphe, start, goal):
            avisite = deque()
            avisite.append(start)  # la liste des noeuds à visiter
            visite = []  # la liste noeud déja visité
            while avisite:
                i = avisite.popleft()
                if i not in visite:

                    visite.append(i)
                    avisite.extend(graphe[i])  # sucesseurs de i

                    if i == goal:
                        break
            return visite

# bfs = BFS(graphe)
# print(bfs.rechercherBFS(graphe, 'A', 'D'))