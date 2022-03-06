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



my_hash_table = HashTable(10)
my_hash_table.put(1, 'hi')
my_hash_table.put(3, 'bye')
my_hash_table.put(5, 'bye')
print(my_hash_table.get(1))
print(my_hash_table._data)
print(my_hash_table.keys())
"""
class HashTable {
  constructor(size){
    this.data = new Array(size);
  }

  _hash(key) {
    let hash = 0;
    for (let i =0; i < key.length; i++){
        hash = (hash + key.charCodeAt(i) * i) % this.data.length
    }
    return hash;
  }
}
"""