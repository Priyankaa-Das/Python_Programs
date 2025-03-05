'''Create an ADT for Queue using OOPs concept(Imagine Python list do not support append and pop).
Define a class with the name Queue and with the following members
- Data member List l
- Data member Size of the array max
- Data member front and rear
Define a member function(constructor) __init__ () which define a list l with the 
entries zeros of size max and initialize front and rear with the value −1.
Define member function Insertion(), to insert new element at the top of the rear.
Define member function Traverse() to display all the values of the queue
Define member function Deletion() to remove an element from front of the queue.'''

class Queue:
    def __init__(self, size):
        self.size = size
        self.l = [0] * size  
        self.front = -1
        self.rear = -1

    def insertion(self, item):
        if self.rear == self.size - 1: 
            print("Queue is full")
            return
        if self.front == -1: 
            self.front = 0
        self.rear += 1
        self.l[self.rear] = item  

    def traverse(self):
        if self.front == -1:
            print("Queue is empty")
            return
        print("The items available are: ", end="")
        for i in range(self.front, self.rear + 1):
            print(self.l[i], end=" ")
        print()

    def deletion(self):
        if self.front == -1 or self.front > self.rear:  
            print("Queue is empty")
            return None
        item = self.l[self.front] 
        self.front += 1
        if self.front > self.rear:  
            self.front = -1
            self.rear = -1
        return item

size = input("Enter the Queue size: ")
obj = Queue(int(size))
while True:
    print("\n1.Insertion\n2.Deletion\n3.Traverse\n4.Exit\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter the item: ")
        obj.insertion(item)
    elif choice == "2":
        item = obj.deletion()
        print("Popped", item)
    elif choice == "3":
        obj.traverse()
    elif choice == "4":
        break