from Graphe import graphe

path = list()

class IDFS():
    path = list()

    # constructeur de la classe BFS
    def __init__(self, graphe):
        self.graphe = graphe

    def DFS(self, currentNode, destination, graph, maxDepth, curList):
        # print("Checking for destination",currentNode)
        curList.append(currentNode)
        if currentNode==destination:
            return True
        if maxDepth<=0:
            global path

            path.append(curList)
            return False
        for node in graph[currentNode]:
            if self.DFS(node,destination,graph,maxDepth-1,curList):
                return True
            else:
                curList.pop()
        return False

    def rechercherIDFS(self, currentNode, destination, graph, maxDepth):
        for i in range(maxDepth):
            curList = list()
            if self.DFS(currentNode, destination, graph, i, curList):
                print("A path exists")
                return path.pop()
        print("Path is not available")
        return False

# idfs = IDFS(graphe)
# if not idfs.iterativeDDFS('A','E',graphe,4):
#     print("Path is not available")
# else:
#     print("A path exists")
#     print(path.pop())