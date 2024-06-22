from Graph import Graph
def test_dfs():
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
    
    # Test DFS from different starting points
    print("DFS starting from vertex 'A':", g.DFS('A'))  # Expected: ['A', 'C', 'E', 'D', 'B'] or similar
    print("DFS starting from vertex 'B':", g.DFS('B'))  # Expected: ['B', 'D', 'E']
    print("DFS starting from vertex 'C':", g.DFS('C'))  # Expected: ['C', 'E', 'D']
    print("DFS starting from vertex 'D':", g.DFS('D'))  # Expected: ['D', 'E']
    print("DFS starting from vertex 'E':", g.DFS('E'))  # Expected: ['E']

    # Additional test case with disconnected components
    g2 = Graph()
    vertices = ['1', '2', '3', '4', '5']
    for vertex in vertices:
        g2.addVertex(vertex)
    
    edges = [
        ('1', '2', 1),
        ('1', '3', 1),
        ('2', '4', 1),
        ('3', '4', 1),
        # Disconnected component
        ('5', '1', 1)
    ]
    for from_vertex, to_vertex, weight in edges:
        g2.addEdge(from_vertex, to_vertex, weight)

    print("DFS starting from vertex '1' in disconnected graph:", g2.DFS('1'))  # Expected: ['1', '3', '4', '2']
    print("DFS starting from vertex '5' in disconnected graph:", g2.DFS('5'))  # Expected: ['5', '1', '3', '4', '2']

    # Test case with cycles
    g3 = Graph()
    vertices = ['X', 'Y', 'Z']
    for vertex in vertices:
        g3.addVertex(vertex)
    
    edges = [
        ('X', 'Y', 1),
        ('Y', 'Z', 1),
        ('Z', 'X', 1)  # Cycle X -> Y -> Z -> X
    ]
    for from_vertex, to_vertex, weight in edges:
        g3.addEdge(from_vertex, to_vertex, weight)
    
    print("DFS starting from vertex 'X' in cyclic graph:", g3.DFS('X'))  # Expected: ['X', 'Y', 'Z']

if __name__ == "__main__":
    test_dfs()
