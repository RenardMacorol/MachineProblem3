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
    
    

