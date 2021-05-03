l = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    
l = [
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]]

# https://py.checkio.org/en/mission/open-labyrinth/

# Graph class, adjacency list representation
class Graph():
    def __init__(self):
        self.adjacencyList = {}

    def addNode(self, node):
        self.adjacencyList[node] = []

    def addEdge(self, node1, node2):
        self.adjacencyList[node1].append(node2)
        self.adjacencyList[node2].append(node1)

# convert 2d maze array to graph
def mazeToGraph(maze):
    graph = Graph()
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            node = (i, j)
            graph.addNode(node)
            if i > 0 and maze[i][j] == 0 and maze[i-1][j] == 0:
                nodeLeft = (i-1,j)
                graph.addEdge(node,nodeLeft)
            if j > 0 and maze[i][j] == 0 and maze[i][j-1] == 0:
                nodeTop = (i,j-1)
                graph.addEdge(node,nodeTop)
    return graph

# find shortes route using BFS algh
def shortestPathBFS(graph, node1, node2):
    # return empty list if node exist and has any edges
    if node1 not in graph.adjacencyList.keys() or node2 not in graph.adjacencyList.keys() or len(graph.adjacencyList[node1]) == 0 or len(graph.adjacencyList[node2]) == 0:
        return []

    queue = []
    queue.append(node1)
    markedNodes = {}
    nodesPath = {}

    for node in graph.adjacencyList.keys():
        markedNodes[node] = 0
        nodesPath[node] = []
    while len(queue) > 0:
        node = queue[0]
        queue.pop(0)

        if node == node2:
            return nodesPath[node2] + [node2] 

        for adjNode in graph.adjacencyList[node]:
            if markedNodes[adjNode] != 1:
                markedNodes[adjNode] = 1
                nodesPath[adjNode].append(node)
                nodesPath[adjNode][:0] = nodesPath[node]
                queue.append(adjNode)
    return []

def cordsToDirections(cordsList):
    route = ""
    for i in range(len(cordsList)-1):
        node1 = cordsList[i]
        node2 = cordsList[i+1]
        if node1[0] - node2[0] == 1:
            route += "N"
        elif node2[0] - node1[0] == 1:
            route += "S"
        elif node1[1] - node2[1] == 1:
            route += "W"
        elif node2[1] - node1[1] == 1:
            route +="E"
    return route

test = mazeToGraph(l)  
print(shortestPathBFS(test,(1,1),(10,10)))
print(cordsToDirections(shortestPathBFS(test,(1,1),(10,10))))