import random
UNVISITED = -1

with open("edges.txt", "r") as file:
    AllEdges = [line.replace('\n','').split('\t', 2) for line in file.readlines()]
    for edge in AllEdges:
        edge[2] = int(edge[2])
    file.close()

class Edge:
    def __init__(self, src, dest, weight):
        self._src = src
        self._dest = dest
        self._weight = weight

    def __del__(self):
        del self

class SCC:
    def __init__(self, n):
        self.sccCount = 0

        self._disc = [UNVISITED] * n    # Stores discovery times of visited vertices
        self.__low = [UNVISITED] * n     # Earliest visited vertex (the vertex with minimum
                                                # discovery time) that can be reached from subtree
                                                # rooted with current vertex
        self.__stack = [False] * n       # To check whether a vertex is in stack
        self.__st = []                   # To store all the connected ancestors
        self.__Time = 0

    def __del__(self):
        del self

    def findSCC(self, u, vertices, graph):
        self._disc[u] = self.__low[u] = self.__Time
        self.__Time += 1
        self.__stack[u] = True

        u_name = vertices[u]
        self.__st.append(u_name)

        for v in graph[u_name]:
            v_index = vertices.index(v[0])
            if self._disc[v_index] == UNVISITED:
                self.findSCC(v_index, vertices, graph)
                self.__low[u] = min(self.__low[u], self.__low[v_index])
            elif self.__stack[v_index] == True:
                self.__low[u] = min(self.__low[u], self._disc[v_index])
            
        if self.__low[u] == self._disc[u]:
            t_index = -1

            while t_index != u:
                t = self.__st.pop()
                t_index = vertices.index(t)
                self.__stack[t_index] = False
                self.__low[t_index] = self._disc[u]
                print(t, end = " ")
            print()
            self.sccCount += 1

class DirectedGraph:
    def __init__(self):
        self.graph = dict(list())
        self.__numVertices = 0  # number of vertices in the graph
        self.__numEdges = 0     # number of edges in the graph
        self.__vertices = []
        self.__newVertices = [] # to add new vertex input by user

        # default edges
        self.__d_edges = [Edge('DMS', 'BST', 619), Edge('DMS', 'BGK', 14113), Edge('BST', 'LDN', 5265), 
                            Edge('BGK', 'MIP', 13338), Edge('MIP', 'LDN', 6456)]

    def __del__(self):
        self.reset()
        del self

    def numVertices(self):
        return self.__numVertices

    def numEdges(self):
        return self.__numEdges

    def addVertex(self, v):
        self.__vertices.append(v)
        self.__numVertices += 1
    
    def addNewVertex(self, v):
        if v in self.__vertices:
            print(f"The vertex {v} already exists in the graph.")
            return

        self.__vertices.append(v)
        self.__numVertices += 1
        self.graph[v] = []
        
        dist = {}
        for key in self.graph.keys():
            if key != v:
                invalidInput = 1
                while (invalidInput):
                    try:
                        dist[key] = int(input("Distance between "+v+" and "+key+": "))
                        invalidInput = 0
                    except ValueError:
                        print("Error: Input is not a whole number.")
                self.__newVertices.append([v,key,(int(dist[key]))])
                self.__newVertices.append([key,v,(int(dist[key]))])
                AllEdges.append([v,key,(int(dist[key]))])
                AllEdges.append([key,v,(int(dist[key]))])

    def addEdge(self, e):
        self.graph[e._src].append((e._dest, e._weight))
        self.__numEdges += 1

    def addNewEdge(self,src,dest):
        exist = False
        for i in range(len(self.graph[src])):
            if dest == self.graph[src][i][0]:
                print("\nEdge between " + src + " & " + dest + " has already existed.")
                exist = True

        if exist == False:
            for i in AllEdges:
                if (src == i[0] and dest == i[1]):
                    weight = i[2]
                    self.graph[src].append((dest, int(weight)))
                    self.__numEdges += 1
                    print("\nEdge between " + src + " & " + dest + " has been added successfully!")
                  
    def removeEdge(self, src, dest):
        for i in range(len(self.graph[src])):
            if dest == self.graph[src][i][0]:
                del self.graph[src][i]
                self.__numEdges -= 1
                print("\nEdge between " + src + " & " + dest + " successfully removed.")
                return

        print("\nEdge between " + src + " & " + dest + " does not exist in the graph.")

    def default(self):
        for edge in self.__d_edges:
            if edge._src not in (self.__vertices or self.graph):
                self.addVertex(edge._src)
                self.graph[edge._src] = []
            if edge._dest not in (self.__vertices or self.graph):
                self.addVertex(edge._dest)
                self.graph[edge._dest] = []
            self.addEdge(edge)
        print("The graph has initialised.")

    def reset(self):
        for i in self.__newVertices:
            if i in AllEdges:
                AllEdges.remove(i)

        self.graph.clear()
        self.__vertices.clear()
        self.__newVertices.clear()
        self.__numVertices = 0
        self.__numEdges = 0
        self.default()

    def randomEdge(self):
        cont = True
        while cont:
            # Case 1: Graph is full, cannot add more edge, hence return
            if self.numEdges() == (len(self.graph) * (len(self.graph) -1)):
                print("Graph has maximum number of edges.")
                return

            # Case 2: Graph is not full and source is in graph, check if the destination exist in the adj list, 
            # if not stop the loop and add edge to graph
            r_edge = random.sample(AllEdges, 1)
            r_tuple = (r_edge[0][1], r_edge[0][2])
            if r_tuple not in self.graph[r_edge[0][0]]:
                cont = False
                self.addEdge(Edge(r_edge[0][0], r_edge[0][1], r_edge[0][2]))
                print(f"Adding random edge {r_edge[0][0]} -> {r_edge[0][1]}")

    def printGraph(self):
        keys = self.graph.keys()
        for key in keys:
            print(f"{key} -> {self.graph[key]}")
    
    def vertexValidation(self, v):
        vertex = 0
        while vertex not in self.__vertices:
            vertex = input(f'Input the {v}      : ')
            if vertex in self.__vertices:
                break
            print("The location is not in the Graph. Please input again")
        return vertex

    def TarjanSCC(self):
        isStronglyConnected = False
        while not isStronglyConnected:
            scc = SCC(self.__numVertices)
            print("The strongly connected components: ")
            for i in range(self.__numVertices):
                if(scc._disc[i] == UNVISITED):
                    scc.findSCC(i, self.__vertices, self.graph)
            print(f"Total: {scc.sccCount}\n\n")
            isStronglyConnected = scc.sccCount == 1
            if isStronglyConnected:
                print("The graph is strongly connected.")
                break
            else:
                print("The graph is not strongly connected.")
                print("Generating random edge...")
                print("----------------------------------------")
                self.randomEdge()
                print()


def userfunctions():
    print("-----------------------------------------------------")
    print("|                    Functions                      |")
    print("| ------------------------------------------------- |")
    print("| Choose to perform:                                |")
    print("| 1. Check if the graph is strongly connected       |")
    print("| 2. Add New Edge                                   |")
    print("| 3. Remove Edge                                    |")
    print("| 4. Add New Vertex                                 |")
    print("| 5. Reset the Graph                                |")
    print("| 6. End program                                    |")
    print("-----------------------------------------------------")

def userinput():
    while True:
        try:
            choice = int(input("Choice: "))
        except ValueError:
                print("This is not a whole number. Input again!")
        else:
            return choice

def main():
    graph = DirectedGraph()
    graph.default()
    print()
    print("Default graph is as follow:")
    graph.printGraph()
    print()

    running = True

    while running:
        userfunctions()
        choice = userinput()
        print()
        while choice:
            if choice == 1:
                print("========================================")
                print("| Function 1: Strongly Connected Graph |")
                print("========================================")
                graph.TarjanSCC()
                break
            
            elif choice == 2:
                print("============================")
                print("| Function 2: Add New Edge |")
                print("============================")
                
                src = graph.vertexValidation("source")
                dest = graph.vertexValidation("destination")
                
                graph.addNewEdge(src, dest)
                
                break
            
            elif choice == 3:
                print("===========================")
                print("| Function 3: Remove Edge |")
                print("===========================")
                
                src = graph.vertexValidation("source")
                dest = graph.vertexValidation("destination")
                
                graph.removeEdge(src, dest)
                break
            
            elif choice == 4:
                print("==============================")
                print("| Function 4: Add New Vertex |")
                print("==============================")
                vert = input('Input the city name : ')
                graph.addNewVertex(vert)
                break
                
            elif choice == 5:
                print("===========================")
                print("| Function 5: Reset Graph |")
                print("===========================")
                graph.reset()
                break
            
            elif choice == 6:
                print("===========================")
                print("| Function 6: End Program |")
                print("===========================")
                running = False
                break
            
            else:
                print("Invalid choice! Input again!")
                userfunctions()
                choice = userinput()
        
        if choice != 6:
            print("_____________________________________________________")
        print()
        print("Current graph is as follow:")
        graph.printGraph()            
        print()
    print("Exiting...")

if __name__ == '__main__':
    main()