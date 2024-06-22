class Graph:
    def __init__(self):
        self.vertex = []
        self.adj_matrix = []
        self.vertex_index_matrix = {}

    def addVertex(self, vertex):
        if vertex in self.vertex_index_matrix:
            print(f'Vertex: {vertex} already exists')
            return

        #Adicionando na matrix de vértices e definindo o indíce do elemento na matriz 
        self.vertex.append(vertex)
        self.vertex_index_matrix[vertex] = len(self.vertex) - 1

        #Expandir matriz de adjacência
        for row in self.adj_matrix:
            row.append(0)
        
        self.adj_matrix.append([0]*len(self.vertex))

    
    def addEdge(self, from_vertex, to_vertex, weight):
        if (from_vertex not in self.vertex_index_matrix) or (to_vertex not in self.vertex_index_matrix):
            print ("One of the vertex passed as parameter isn't present in the graph")
            return
        
        from_index = self.vertex_index_matrix[from_vertex]
        to_index = self.vertex_index_matrix[to_vertex]

        self.adj_matrix[from_index][to_index] = weight
    
    def getVertexIndex(self, vertex):
        return self.vertex_index_matrix[vertex]
    
    def getAdjMatrix(self):
        return self.adj_matrix
    
    def BFS(self, start_vertex):
        if start_vertex not in self.vertex_index_matrix:
            print("The vertex provided isn't present in the graph")
            return
        start_index = self.vertex_index_matrix[start_vertex]
        #Colocando todos os vértices como não visitados
        visited = [False] * len(self.vertex)
        #Fila de quais tem que visitar
        queue = [start_index]
        #Já visita primeiro
        visited[start_index] = True
        #Traversal
        traversal = []
        while queue:
            current_index = queue.pop(0)
            current_vertex = self.vertex[current_index]
            traversal.append(current_vertex)

            for i, is_edge in enumerate(self.adj_matrix[current_index]):
                if (is_edge != 0) and (visited[i] == False):
                    queue.append(i)
                    visited[i] = True
        return traversal
    

    def addEdge(self, from_vertex, to_vertex, weight):
        if (from_vertex not in self.vertex_index_matrix) or (to_vertex not in self.vertex_index_matrix):
            print ("One of the vertex passed as parameter isn't present in the graph")
            return
        
        from_index = self.vertex_index_matrix[from_vertex]
        to_index = self.vertex_index_matrix[to_vertex]

        self.adj_matrix[from_index][to_index] = weight
    
    def getVertexIndex(self, vertex):
        return self.vertex_index_matrix[vertex]
    
    def getAdjMatrix(self):
        return self.adj_matrix
    
    def DFS(self, start_vertex):
        if start_vertex not in self.vertex_index_matrix:
            print("The vertex provided isn't present in the graph")
            return
        start_index = self.vertex_index_matrix[start_vertex]
        #Colocando todos os vértices como não visitados
        visited = [False] * len(self.vertex)
        #Fila de quais tem que visitar
        queue = [start_index]
        #Já visita primeiro
        visited[start_index] = True
        #Traversal
        traversal = []
        while queue:
            #Pop no que acabou de entrar
            current_index = queue.pop()
            current_vertex = self.vertex[current_index]
            traversal.append(current_vertex)

            for i, is_edge in enumerate(self.adj_matrix[current_index]):
                if (is_edge != 0) and (visited[i] == False):
                    queue.append(i)
                    visited[i] = True
        return traversal



