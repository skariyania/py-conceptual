import math
import hashlib
import logging

class BloomFilter:
    def __init__(self, capacity, error_rate=0.001):
        """
        Initialize the Bloom filter.

        :param capacity: The expected number of elements to be added to the filter.
        :param error_rate: The acceptable false positive rate (default is 0.1% or 0.001).
        """
        logging.debug("initializing bloom filter..")
        self.capacity = capacity
        self.error_rate = error_rate
        self.size = self.calculate_size(capacity, error_rate)
        self.num_hash_functions = self.calculate_num_hash_functions(self.size, capacity)
        self.bit_array = [0] * self.size
        
        logging.debug("capacity: %s", self.capacity)
        logging.debug("error_rate: %s", self.error_rate)
        logging.debug("size: %s", self.size)
        logging.debug("num_hash_functions: %s", self.num_hash_functions)
        

    def calculate_size(self, capacity, error_rate):
        """
        Calculate the size of the bit array based on the desired capacity and error rate.

        :param capacity: The expected number of elements.
        :param error_rate: The acceptable false positive rate.
        :return: The size of the bit array.
        """
        size = int(-(capacity * math.log(error_rate)) / (math.log(2) ** 2))
        return max(size, 1) # Ensure a minimum size of 1
    
    def calculate_num_hash_functions(self, size, capacity):
        """
        Calculate the optimal number of hash functions based on the size and capacity.

        :param size: The size of the bit array.
        :param capacity: The expected number of elements.
        :return: The number of hash functions.
        """
        num_hash_functions = int((size / capacity) * math.log(2))
        return max(num_hash_functions, 1) # Ensure a minimum of 1 hash function
    
    def add(self, element):
        """
        Add an element to the Bloom filter.

        :param element: The element to add.
        """
        for i in range(self.num_hash_functions):
            index = self.hash_function(element, i)
            self.bit_array[index] = 1
    
    def contains(self, element):
        """
        Check if the Bloom filter possibly contains the given element.

        :param element: The element to check.
        :return: True if the element is possibly in the set, False otherwise.
        """
        for i in range(self.num_hash_functions):
            index = self.hash_function(element, i)
            if self.bit_array[index] == 0:
                return False
            return True
        
    def hash_function(self, element, index):
        """
        Hash the element using a combination of a string hash and an index.

        :param element: The element to hash.
        :param index: The index of the hash function.
        :return: The hashed index.
        """
        hash_value = hashlib.sha256(str(element).encode("utf-8"))
        hashed_index = int(hash_value.hexdigest(), 16) % self.size
        return (hashed_index + index) % self.size

# Example usage of bloom filter    
def main():
    # setting log level to debug
    logging.basicConfig(level=logging.DEBUG)

    filter_capacity = 1000
    bloom_filter = BloomFilter(filter_capacity)

    # Add elements to bloom filter
    bloom_filter.add("apple")
    bloom_filter.add("Pineapple")
    bloom_filter.add("grape")

    print("it contains apple? ", bloom_filter.contains("apple"))
    print("it contains app? ", bloom_filter.contains("app"))
    print("it contains pine? ", bloom_filter.contains("pine"))

main()
