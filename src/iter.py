class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration()

    def has_next(self):
        return self.index < len(self.data)
    
    def next(self):
        return self.__next__()

class CollectionList:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def create_iterator(self):
        return Iterator(self.data)


# usage
collection = CollectionList()
collection.add_item("apple")
collection.add_item("grape")
collection.add_item("tomato")

iter = collection.create_iterator()
for item in iter:
    print(item)

print("while .. has next")
iter2 = collection.create_iterator()
while iter2.has_next():
    print(iter2.next())
