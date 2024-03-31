#Graph Class
class Graph: 
    #Groud UP Graph
    def __init__(self,num_Vertices):
        self.num_vertices = num_Vertices
        self.adjMatrix = [[0]*num_Vertices for _ in range(num_Vertices)]
        self.vertices = []

    def addEdge(self,source,destination):
        if source >= 0 and source < self.num_vertices and destination >= 0 and destination < self.num_vertices:
            self.adjMatrix[source][destination] =1
    
    def addVertex(self,element):
       self.vertices.append(element)
       
    
    def __str__(self):
        result = "  "
        for vertex in self.vertices:
            result+=str(vertex)+" "
        result += "\n"
        for i in range(self.num_vertices):
            result += str(self.vertices[i])+" "
            for j in range(self.num_vertices):
                result += str(self.adjMatrix[i][j]) + " "
            result += "\n"
        return result
    
    def dfs_traversal(self, start_vertex):
        visited = [False] * self.num_vertices  # Initialize all vertices as not visited
        stack = []  # Create a stack for DFS
        result = []  # List to store the DFS traversal result

        stack.append(start_vertex)  # Push the start vertex onto the stack

        while stack:
            current_vertex = stack.pop()  # Pop a vertex from the stack
            if not visited[current_vertex]:
                result.append(self.vertices[current_vertex])  # Visit the current vertex
                visited[current_vertex] = True

            # Visit all adjacent vertices of the current vertex
            for neighbor in range(self.num_vertices):
                if self.adjMatrix[current_vertex][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)  # Push the adjacent vertex onto the stack

        return result
    
    def topological_sort(self):
        visited = [False] * self.num_vertices
        stack = []

        for i in range(self.num_vertices):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        return stack[::-1]  # Return the reverse of the stack for topological order

    def topological_sort_util(self, vertex, visited, stack):
        visited[vertex] = True

        for neighbor in range(self.num_vertices):
            if self.adjMatrix[vertex][neighbor] == 1 and not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        stack.append(self.vertices[vertex])
    
    

#Note! All of this are dag
print("Normal DAG")
g1 = Graph(7)
g1.addVertex("A")#0
g1.addVertex("B")#1
g1.addVertex("C")#2
g1.addVertex("D")#3
g1.addVertex("E")#4
g1.addVertex("F")#5
g1.addVertex("G")#6

g1.addEdge(0,1)
g1.addEdge(0,2)
g1.addEdge(1,3)
g1.addEdge(2,3)
g1.addEdge(3,4)
g1.addEdge(4,5)
g1.addEdge(4,6)
g1.addEdge(5,6)

print(g1.__str__())

print("Multiple Root DAG")
g2 = Graph(5)
g2.addVertex("A")#0
g2.addVertex("B")#1
g2.addVertex("C")#2
g2.addVertex("D")#3
g2.addVertex("E")#4

g2.addEdge(0,1)
g2.addEdge(1,2)
g2.addEdge(2,3)
g2.addEdge(3,4)
g2.addEdge(0,3)

print(g2.__str__())

print("DAG with Cycle")
g3 = Graph(5)
g3.addVertex("A")#0
g3.addVertex("B")#1
g3.addVertex("C")#2
g3.addVertex("D")#3
g3.addVertex("E")#4

g3.addEdge(0,1)
g3.addEdge(1,2)
g3.addEdge(2,3)
g3.addEdge(3,4)
g3.addEdge(4,0) # This edge creates a cycle

print(g3.__str__())

print("DAG with one Vertex")
g4 = Graph(1)
g4.addVertex("A")#0

print(g4.__str__())

print("DAG Disconnected")
g5 = Graph(7)
g5.addVertex("A")#0
g5.addVertex("B")#1
g5.addVertex("C")#2
g5.addVertex("D")#3
g5.addVertex("E")#4
g5.addVertex("F")#5
g5.addVertex("G")#6

g5.addEdge(0,1)
g5.addEdge(1,2)
g5.addEdge(2,3)
g5.addEdge(3,4)
g5.addEdge(4,5)
g5.addEdge(5,6)

# Disconnected component
g5.addEdge(0,6)

print(g5.__str__())

# Example usage of the dfs method (Make a code where it can put any vertex starting point by the user)
print("DFS traversal starting from vertex 'A':", g1.dfs_traversal(0))
print("DFS traversal starting from vertex 'A':", g2.dfs_traversal(0))
print("DFS traversal starting from vertex 'A':", g3.dfs_traversal(0))
print("DFS traversal starting from vertex 'A':", g4.dfs_traversal(0))
print("DFS traversal starting from vertex 'A':", g5.dfs_traversal(0))
# Note that these are only starting from vertex A (Make a code where it can put any vertex starting point by the user)
print()
print("Topological Sort starting from vertex 'A':", g1.topological_sort())
print("Topological Sort starting from vertex 'A':", g2.topological_sort())
print("Topological Sort starting from vertex 'A':", g3.topological_sort())
print("Topological Sort starting from vertex 'A':", g4.topological_sort())
print("Topological Sort starting from vertex 'A':", g5.topological_sort())