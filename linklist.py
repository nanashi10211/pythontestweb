import math

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
    def insertAtBegin(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        oldHead = self.head
        self.head = newNode
        newNode.next = oldHead
    def insertAtEnd(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
            return 
        oldHead = self.head
        while(oldHead.next):
            oldHead = oldHead.next
        oldHead.next = newNode
    def insertAtMid(self,data):
        newNode = Node(data)
        count = 1
        head = self.head
        while(head.next):
            head = head.next
            count+=1
        count = math.floor(count/2)
        head = self.head
        while(count > 0):
            head = head.next
            count -= 1
   
        oldNode = head.next
        oldNext = head.next.next
        head.next = newNode
        newNode.next = oldNext

    
    def printList(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.next



def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key

if __name__ == "__main__":
    list = List()
    arr = [12, 11, 13, 5, 6]
    print(arr)
    insertionSort(arr)
    print(arr)
