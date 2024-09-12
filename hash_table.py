class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if key already exists
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
                return

# Example usage
if __name__ == "__main__":
    hash_table = HashTable(10)
    hash_table.insert('apple', 10)
    hash_table.insert('banana', 20)
    print("Search apple:", hash_table.search('apple'))
    hash_table.delete('apple')
    print("Search apple after deletion:", hash_table.search('apple'))
