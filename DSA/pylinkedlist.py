import random

Node_count = 0
Nodes = dict()

class Node:
    def __init__(self, data) -> None:
         self.data = data
         self.next = None
    
    def nextNode(self, nextnode):
        self.next = nextnode

    def getData(self):
        return self.data

    def getNextNodeData(self):
        try:
            return self.next.getData()
        except AttributeError:
            return None


def addEleInLinkedList(ele):
    global Node_count
    Node_count += 1
    Nodes[Node_count] = Node(ele)


### ADDING NODES 
for i in range(5):
    addEleInLinkedList(random.randint(1, 1000))
    # if not first node then add reference to last node in self.next
    if Node_count > 1:
        Nodes[Node_count - 1].nextNode(Nodes[Node_count])

## PRINTING NODES WITH THEIR DATA
for index, nodes in Nodes.items():
    print(f"{index}: {nodes.getData()} || Next Node data: {nodes.getNextNodeData()}" )
