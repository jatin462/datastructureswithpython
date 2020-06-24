class Hashtable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.max

    def __set__(self, key, value):
        hash_value = self.get_hash(key=key)
        count = 0
        while count < self.max:
            if self.arr[hash_value] is not None:
                hash_value += 1
                if hash_value > self.max - 1:
                    hash_value = 0
            elif self.arr[hash_value] is None:
                self.arr[hash_value] = value
                break

t = Hashtable()
t.__set__("march 16", 15)
t.__set__("march 17", 18)
t.__set__("march 18", 19)
t.__set__("march 6", 20)
print(t.arr)
