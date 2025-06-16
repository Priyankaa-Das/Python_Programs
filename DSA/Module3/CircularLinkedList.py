'''Implement Circular Linked List in python using the following information:
Create class node with the members data and next. Develop a class
CirLinkedlist with the following members:
Data member start
Define function __init__() to initialize the object of class CirLinkedList
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
        self.next = None

class CirLinkedList:
    def __init__(self):
        self.start = None

    def InsertBegining(self, item):
        new_node = Node(item)
        if not self.start:
            new_node.next = new_node
            self.start = new_node
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            new_node.next = self.start
            temp.next = new_node
            self.start = new_node
        print("Insertion success!!!")

    def InsertEnd(self, item):
        new_node = Node(item)
        if not self.start:
            new_node.next = new_node
            self.start = new_node
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.start
        print("Insertion success!!!")

    def InsertSpecified(self, item, location):
        if not self.start:
            print("List is empty. Inserting at beginning.")
            self.InsertBegining(item)
            return
        temp = self.start
        while temp.data != location and temp.next != self.start:
            temp = temp.next
        if temp.data != location:
            print("Given node not found in the list!!!")
            return
        new_node = Node(item)
        new_node.next = temp.next
        temp.next = new_node
        print("Insertion success!!!")

    def DeleteStart(self):
        if not self.start:
            print("List is Empty!!! Deletion not possible!!!")
            return
        if self.start.next == self.start:
            self.start = None
        else:
            temp = self.start
            last = self.start
            while last.next != self.start:
                last = last.next
            self.start = self.start.next
            last.next = self.start
            del temp
        print("Deletion success!!!")

    def DeleteEnd(self):
        if not self.start:
            print("List is Empty!!! Deletion not possible!!!")
            return
        temp = self.start
        if temp.next == self.start:
            self.start = None
        else:
            prev = None
            while temp.next != self.start:
                prev = temp
                temp = temp.next
            prev.next = self.start
        del temp
        print("Deletion success!!!")

    def DeleteSpecified(self, item):
        if not self.start:
            print("List is Empty!!! Deletion not possible!!!")
            return
        temp = self.start
        prev = None
        while temp.data != item and temp.next != self.start:
            prev = temp
            temp = temp.next
        if temp.data != item:
            print("Given node not found in the list!!!")
            return
        if temp == self.start:
            self.DeleteStart()
            return
        prev.next = temp.next
        del temp
        print("Deletion success!!!")

    def traverse(self):
        if not self.start:
            print("List is Empty!!!")
            return
        print("Start --> ", end="")
        temp = self.start
        while True:
            print(f"{temp.data} --> ", end="")
            temp = temp.next
            if temp == self.start:
                break
        print("Start")

    def Reverse(self):
        if not self.start or self.start.next == self.start:
            return
        prev = None
        current = self.start
        next_node = None
        first = self.start
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.start:
                break
        first.next = prev
        self.start = prev
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
cll = CirLinkedList()

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
                cll.InsertBegining(item)
            elif choice2 == '2':
                item = int(input("Enter item to insert at end: "))
                cll.InsertEnd(item)
            elif choice2 == '3':
                item = int(input("Enter item to insert: "))
                location = int(input("Enter the node item after which to insert: "))
                cll.InsertSpecified(item, location)
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
                cll.DeleteStart()
            elif choice2 == '2':
                cll.DeleteEnd()
            elif choice2 == '3':
                item = int(input("Enter item to delete: "))
                cll.DeleteSpecified(item)
            elif choice2 == '4':
                break
            else:
                print("Please select correct Deleting option!!!")
    elif choice1 == '3':
        cll.traverse()
    elif choice1 == '4':
        cll.Reverse()
    elif choice1 == '5':
        item = int(input("Enter item to search: "))
        cll.Search(item)
    elif choice1 == '6':
        print("Exiting program...")
        break
    else:
        print("Please select correct main menu option!!!")
    print("\n")