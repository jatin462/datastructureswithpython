class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class linkedList:
    def __init__(self):
        self.head = None

    def sort(self, data):
        if self.head is None:
            n = Node(data, None)
            self.head = n
            return

        current_node = self.head

        if current_node.data > data:
            n = Node(data, current_node)
            self.head = n
            return

        while current_node.next is not None:
            if current_node.next.data > data:
                break
            current_node = current_node.next

        n = Node(data, current_node.next)
        current_node.next = n
        return

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)


ll = linkedList()
num = int(input("enter number"))
while num != -1:
    ll.sort(num)
    num = int(input("Enter Number"))

ll.print()



