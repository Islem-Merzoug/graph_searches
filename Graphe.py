from Noeud import Node

# instencier les objets node comme en java quand on fait: node node1 = new node('A')
Node1 = Node('A')
Node2 = Node('B')
Node3 = Node('C')
Node4 = Node('D')
Node5 = Node('E')
Node6 = Node('F')

# creation du graphe statique a partir des noeuds créé la haut
graphe = {
    Node1.nom: [Node2.nom, Node3.nom],
    Node2.nom: [Node4.nom, Node5.nom],
    Node3.nom: [Node6.nom],
    Node4.nom: [],
    Node5.nom: [],
    Node6.nom: []
}

adjacency_list = {
    Node1.nom: [(Node2.nom, 1), (Node3.nom, 3), (Node4.nom, 7)],
    Node2.nom: [(Node4.nom, 5)],
    Node3.nom: [(Node4.nom, 12)]
}

# class grave pour pouvoir creer des objets graphe
class Graphe:
    # constructeur de la classe Graphe
    def __init__(self, graphe):
        self.graphe = graphe

    def printGraphe(self):
        print(self.graphe)

# grapheO = Graphe(graphe)
# grapheO.printGraphe()