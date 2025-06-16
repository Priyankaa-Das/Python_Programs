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

    def insertion_rear(self, item):
        if self.rear == self.size - 1:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.l[self.rear] = item

    def insertion_front(self, item):
        if self.front <= 0:
            print("Cannot insert at front")
            return
        self.front -= 1
        self.l[self.front] = item

    def insertion_middle(self, item):
        if self.rear == self.size - 1:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        mid = (self.front + self.rear) // 2 + 1
        for i in range(self.rear, mid - 1, -1):
            self.l[i + 1] = self.l[i]
        self.l[mid] = item
        self.rear += 1

    def deletion_front(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
            return
        item = self.l[self.front]
        self.front += 1
        if self.front > self.rear:
            self.front = self.rear = -1
        return item

    def deletion_rear(self):
        if self.front == -1 or self.rear < self.front:
            print("Queue is empty")
            return
        item = self.l[self.rear]
        self.rear -= 1
        if self.rear < self.front:
            self.front = self.rear = -1
        return item

    def deletion_middle(self):
        if self.front == -1 or self.rear < self.front:
            print("Queue is empty")
            return
        mid = (self.front + self.rear) // 2
        item = self.l[mid]
        for i in range(mid, self.rear):
            self.l[i] = self.l[i + 1]
        self.rear -= 1
        if self.rear < self.front:
            self.front = self.rear = -1
        return item

    def traverse(self):
        if self.front == -1 or self.rear < self.front:
            print("Queue is empty")
            return
        print("The items available are:", end=" ")
        for i in range(self.front, self.rear + 1):
            print(self.l[i], end=" ")
        print()


size = int(input("Enter the Queue size: "))
obj = Queue(size)

while True:
    print("\n1. Insertion")
    print("2. Deletion")
    print("3. Traverse")
    print("4. Exit\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\na. Insert at Front")
        print("b. Insert at Middle")
        print("c. Insert at Rear")
        sub_choice = input("Enter your insertion choice: ").lower()
        item = input("Enter the item: ")
        if sub_choice == 'a':
            obj.insertion_front(item)
        elif sub_choice == 'b':
            obj.insertion_middle(item)
        elif sub_choice == 'c':
            obj.insertion_rear(item)
        else:
            print("Invalid insertion choice!")

    elif choice == "2":
        print("\na. Delete from Front")
        print("b. Delete from Middle")
        print("c. Delete from Rear")
        sub_choice = input("Enter your deletion choice: ").lower()
        if sub_choice == 'a':
            item = obj.deletion_front()
        elif sub_choice == 'b':
            item = obj.deletion_middle()
        elif sub_choice == 'c':
            item = obj.deletion_rear()
        else:
            print("Invalid deletion choice!")
            continue
        if item is not None:
            print("Popped:", item)

    elif choice == "3":
        obj.traverse()

    elif choice == "4":
        break

    else:
        print("Invalid main menu choice!")