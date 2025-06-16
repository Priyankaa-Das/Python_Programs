'''Implement Doubly Circular Linked List in python using the following
information:
Create class node with the members data and next. Develop a class
DblCirLinkedlist with the following members:
Data member start
Define function __init__() to initialize the object of class DblCirLinkedList
Define a function InsertBegining() to insert a new node in the beginning of
the linked list
Define a function InsertEnd() to insert at the end of the linked list
Define a function InsertSpecified() to insert at specified position
Define a function DeleteStart() to delete the start node
Define a function DeleteEnd() to delete from the end.
Define a function DeleteSpecified() to delete specified node
Define a function traverse() to display all the data of the linked list.
Define a function Reverse() to reverse the order of the nodes in the linked list
Define a function Search() to search an element of the linked list'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DblCirLinkedList:
    def __init__(self):
        self.start = None

    def InsertBeginning(self, item):
        new_node = Node(item)
        if not self.start:
            new_node.next = new_node.prev = new_node
            self.start = new_node
        else:
            last = self.start.prev
            new_node.next = self.start
            new_node.prev = last
            self.start.prev = new_node
            last.next = new_node
            self.start = new_node
        print("Insertion success!!!")

    def InsertEnd(self, item):
        new_node = Node(item)
        if not self.start:
            new_node.next = new_node.prev = new_node
            self.start = new_node
        else:
            last = self.start.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.start
            self.start.prev = new_node
        print("Insertion success!!!")

    def InsertSpecified(self, item, location):
        if not self.start:
            print("List is empty. Inserting at beginning.")
            self.InsertBeginning(item)
            return
        temp = self.start
        while temp.data != location and temp.next != self.start:
            temp = temp.next
        if temp.data != location:
            print("Given node not found in the list!!!")
            return
        new_node = Node(item)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node
        print("Insertion success!!!")

    def DeleteStart(self):
        if not self.start:
            print("List is Empty!!! Deletion not possible!!!")
            return
        if self.start.next == self.start:
            self.start = None
        else:
            last = self.start.prev
            temp = self.start
            self.start = self.start.next
            self.start.prev = last
            last.next = self.start
            del temp
        print("Deletion success!!!")

    def DeleteEnd(self):
        if not self.start:
            print("List is Empty!!! Deletion not possible!!!")
            return
        if self.start.next == self.start:
            self.start = None
        else:
            last = self.start.prev
            second_last = last.prev
            second_last.next = self.start
            self.start.prev = second_last
            del last
        print("Deletion success!!!")

    def DeleteSpecified(self, item):
        if not self.start:
            print("List is Empty!!! Deletion not possible!!!")
            return
        temp = self.start
        while temp.data != item and temp.next != self.start:
            temp = temp.next
        if temp.data != item:
            print("Given node not found in the list!!!")
            return
        if temp == self.start:
            self.DeleteStart()
            return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        del temp
        print("Deletion success!!!")

    def traverse(self):
        if not self.start:
            print("List is Empty!!!")
            return
        print("Start --> ", end="")
        temp = self.start
        while True:
            print(f"{temp.data} <-> ", end="")
            temp = temp.next
            if temp == self.start:
                break
        print("Start")

    def Reverse(self):
        if not self.start or self.start.next == self.start:
            return
        temp = self.start
        prev_node = None
        while True:
            next_node = temp.next
            temp.next, temp.prev = temp.prev, temp.next
            prev_node = temp
            temp = next_node
            if temp == self.start:
                break
        self.start = prev_node
        print("List reversed!!!")

    def Search(self, item):
        if not self.start:
            print("List is Empty!!!")
            return
        temp = self.start
        while True:
            if temp.data == item:
                print(f"{item} found in the list!!!")
                return
            temp = temp.next
            if temp == self.start:
                break
        print(f"{item} not found in the list!!!")


# --- MENU DRIVEN PROGRAM ---
dll = DblCirLinkedList()

while True:
    print("\n*********** MENU *************")
    print("1. Insert\n2. Delete\n3. Display\n4. Reverse\n5. Search\n6. Exit")
    choice1 = input("Enter your choice: ")

    if choice1 == '1':
        while True:
            print("\nSelect from the following Inserting options")
            print("1. At Beginning\n2. At End\n3. After a Node\n4. Cancel")
            choice2 = input("Enter your choice: ")
            if choice2 == '1':
                item = int(input("Enter item to insert at beginning: "))
                dll.InsertBeginning(item)
            elif choice2 == '2':
                item = int(input("Enter item to insert at end: "))
                dll.InsertEnd(item)
            elif choice2 == '3':
                item = int(input("Enter item to insert: "))
                location = int(input("Enter the node item after which to insert: "))
                dll.InsertSpecified(item, location)
            elif choice2 == '4':
                break
            else:
                print("Please select correct Inserting option!!!")

    elif choice1 == '2':
        while True:
            print("\nSelect from the following Deleting options")
            print("1. At Beginning\n2. At End\n3. Specific Node\n4. Cancel")
            choice2 = input("Enter your choice: ")
            if choice2 == '1':
                dll.DeleteStart()
            elif choice2 == '2':
                dll.DeleteEnd()
            elif choice2 == '3':
                item = int(input("Enter item to delete: "))
                dll.DeleteSpecified(item)
            elif choice2 == '4':
                break
            else:
                print("Please select correct Deleting option!!!")

    elif choice1 == '3':
        dll.traverse()
    elif choice1 == '4':
        dll.Reverse()
    elif choice1 == '5':
        item = int(input("Enter item to search: "))
        dll.Search(item)
    elif choice1 == '6':
        print("Exiting program...")
        break
    else:
        print("Please select correct main menu option!!!")
    print("\n")