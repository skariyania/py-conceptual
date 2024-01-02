import heapq
from collections import defaultdict

class MaxFrequencyStack:
    def __init__(self):
        self.stack = []
        self.frequency = defaultdict(int)
        self.max_heap = []

    def push(self, element):
        self.frequency[element] +=1
        freq = self.frequency[element]
        heapq.heappush(self.max_heap, (-freq, -element))
        self.stack.append(element)
    
    def pop(self):
        if not self.stack:
            return None
        
        _, element = heapq.heappop(self.max_heap)
        self.frequency[element] -= 1
        self.stack.pop()
        return -element

# Example usage
stack = MaxFrequencyStack()
stack.push(4)
stack.push(6)
stack.push(7)
stack.push(6)
stack.push(8)

print("1. pop() => returns {}", stack.pop()) # Output: 6
print("2. pop() => returns {}", stack.pop()) # Output: 8
print("3. pop() => returns {}", stack.pop()) # Output: 7