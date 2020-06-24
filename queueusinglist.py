class queue:
    def __init__(self):
        self.queue1 = []

    def insert(self, element):
        self.queue1.append(element)

    def pop(self):
        self.queue1.pop(0)

    def print_element(self):
        print(self.queue1)

a = queue()
a.insert(2)
a.insert(3)
a.insert(4)
a.print_element()
a.pop()
a.pop()
a.print_element()