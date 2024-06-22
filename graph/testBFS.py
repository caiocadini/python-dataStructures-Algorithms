from Graph import Graph
def test_bfs_directed():
    # Create a directed graph instance
    g = Graph()
    
    # Add vertices
    vertices = ['A', 'B', 'C', 'D', 'E']
    for vertex in vertices:
        g.addVertex(vertex)
    
    # Add directed edges
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 1),
        ('B', 'D', 1),
        ('C', 'D', 1),
        ('D', 'E', 1),
        ('C', 'E', 1)
    ]
    for from_vertex, to_vertex, weight in edges:
        g.addEdge(from_vertex, to_vertex, weight)
    
    # Test BFS from different starting points
    print("BFS starting from vertex 'A':", g.BFS('A'))  # Should visit in order respecting directed edges
    print("BFS starting from vertex 'B':", g.BFS('B'))  # Should visit B -> D -> E
    print("BFS starting from vertex 'C':", g.BFS('C'))  # Should visit C -> D -> E
    print("BFS starting from vertex 'D':", g.BFS('D'))  # Should visit D -> E
    print("BFS starting from vertex 'E':", g.BFS('E'))  # Should visit only E as it's a terminal node

    # Additional test: Starting from a vertex with no outgoing edges
    g_no_outgoing = Graph()
    g_no_outgoing.addVertex('X')
    g_no_outgoing.addVertex('Y')
    g_no_outgoing.addEdge('X', 'Y', 1)  # X -> Y
    
    print("BFS starting from vertex 'Y' (no outgoing edges):", g_no_outgoing.BFS('Y'))  # Should only return ['Y']

if __name__ == "__main__":
    test_bfs_directed()
