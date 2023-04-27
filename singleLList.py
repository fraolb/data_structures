class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLList:
    def __init__(self):
        self.head = None
    def add(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def countList(self):
        count = 0
        temp = self.head

        while(temp):
            count +=1
            temp= temp.next
        return count

list = SingleLList()

list.add(1)
list.add(2)

print(list.countList())
