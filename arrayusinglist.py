class array2:
    def __init__(self):
        self.array1 = []

    def insert(self, element):
        self.array1.append(element)

    def pop(self):
        self.array1.pop()

    def print_element(self):
        print(self.array1)

a = array2()
a.insert(2)
a.insert(3)
a.insert(4)
a.print_element()
a.pop()
a.pop()
a.print_element()