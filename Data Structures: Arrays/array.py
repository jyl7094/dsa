class Array:
    def __init__(self):
        self._length = 0
        self._data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self._data[index]
    
    def push(self, item):
        self._data[self._length] = item
        self._length += 1
        return self._length
    
    def pop(self):
        last_item = self._data[self._length-1]
        del self._data[self._length-1]
        self._length -= 1
        return last_item

    def delete(self, index):
        item = self._data[index]
        for i in range(index, self._length-1):
            self._data[i] = self._data[i+1]
            
        del self._data[self._length-1]
        self._length -= 1
        return item
