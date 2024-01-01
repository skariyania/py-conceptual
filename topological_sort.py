from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, curr, visited, is_cyclic):
        visited[curr] = 1

        for x in self.graph[curr]:
            if visited[x] == 1:
                is_cyclic[0] = True
                return
            elif visited[x] == 0:
                self.dfs(x, visited, is_cyclic)
        
        visited[curr] = 2

    def check_cycle(self):
        visited = [0] * self.V
        is_cycle = [False]

        for i in range(self.V):
            if visited[i] == 0:
                self.dfs(i, visited, is_cycle)

        return is_cycle[0]
    
    def topological_sort_util(self, u, visited, stack):
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.topological_sort_util(v, visited, stack)
        stack.append(u)

    def topological_sort(self):
        stack = []
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        result = []
        while stack:
            result.append(chr(stack.pop() + ord('a')))
        return result
    
def print_order(words):
    frq = [0] * 26
    k = 0

    for word in words:
        for char in word:
            frq[ ord(char) - ord('a') ] += 1
            if frq[ ord(char) - ord('a')] == 1:
                k += 1

    graph = Graph(k)
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        j = 0
        while j < len(word1) and j < len(word2):
            if word1[j] != word2[j]:
                u = ord(word1[j]) - ord('a')
                v = ord(word2[j]) - ord('a')
                graph.add_edge(u, v)
                break
            j += 1
    
    if graph.check_cycle():
        print("Valid order is not possible")
    else:
        order = graph.topological_sort()
        print("order of characters is", order)

# Driver code
if __name__ == "__main__":
    words = ["baa", "abcd", "abca", "cab", "cad"]
    print_order(words)
