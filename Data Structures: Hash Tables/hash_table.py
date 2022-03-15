# Hash table with separate chaining
class HashTable:
    def __init__(self, size):
        self._data = [None] * size
    
    def __str__(self):
        return str(self._data)
    
    def _hash(self, key):
        hash = 0
        str_key = str(key)
        for i in range(len(str_key)):
            hash = (hash + ord(str_key[i]) * i) % len(self._data)
        return hash

    def put(self, key, value):
        hash = self._hash(key)
        if not self._data[hash]:
            self._data[hash] = [[key, value]]
        else:
            for elem in self._data[hash]:
                if elem[0] == key:
                    elem[1] = value
                    return
            self._data[hash].append([key, value])

    def get(self, key):
        hash = self._hash(key)
        for elem in self._data[hash]:
            if elem[0] == key:
                return elem[1]
        return None

    def keys(self):
        k = set()
        for hash in self._data:
            if hash is None:
                continue
            for elem in hash:
                k.add(elem[0])
        return k
