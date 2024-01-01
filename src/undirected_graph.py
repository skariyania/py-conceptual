class UndirectedGraph:
    def __init__(self):
        self.undirected_graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.undirected_graph:
            self.undirected_graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # adding edges in both direction as undirected graph
        self.undirected_graph[vertex1].append(vertex2)
        self.undirected_graph[vertex2].append(vertex1)

    def display(self):
        for vertex, neighbors in self.undirected_graph.items():
            print(f"{vertex}: {neighbors}")

# Example usage
if __name__ == "__main__":
    g = UndirectedGraph()

    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")


    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "D")
    g.add_edge("D", "A")

    g.display()
