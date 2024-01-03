from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.frequency = defaultdict(int)
        self.min_frequency = 0

    def get(self, key):
        if key in self.cache:
            self.frequency[key] += 1
            self.min_frequency = min(self.min_frequency, self.frequency[key])
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if self.capacity == 0:
            return
        
        if len(self.cache) >= self.capacity:
            keys_to_remove = [k for k, v in self.frequency.items() if v == self.min_frequency]
            for k in keys_to_remove:
                del self.cache[k]
                del self.frequency[k]

        self.cache[key] = value

    def list(self):
        return self.cache

# Example usage
        
if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put("apple", "fruit")
    print("add: apple", cache.list())

    cache.put("pineapple", "fruit")
    print("add: pineapple", cache.list())

    cache.put("apple", "fruit")
    print("add: apple again", cache.list())

    # get an apple
    print("LFU get: ", cache.get("apple"))
    
    cache.put("grape", "fruit")
    print("add: grape", cache.list())

    cache.put("banana", "fruit")
    print("add: banana", cache.list())

    # get an apple again
    print("LFU get: ", cache.get("apple"))

