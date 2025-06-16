'''Implement Doubly Linked List in python using the following information:
Create class node with the members data and next. Develop a class
DblLinkedlist with the following members:
Data member start
Define function __init__() to initialize the object of class DblLinkedList
Define a function InsertBegining() to insert a new node in the beginning of the linked list
Define a function InsertEnd() to insert at the end of the linked list
Define a function InsertSpecified() to insert at specified position
Define a function DeleteStart() to delete the start node
Define a function DeleteEnd() to delete from the end.
Define a function DeleteSpecified() to delete specified node
Define a function traverse() to traverse all the data of the linked list.
Define a function Reverse() to reverse the order of the nodes in the linked list
Define a function Search() to search an element of the linked list'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def _init_(self):
        self.head = None

    def InsertBegining(self, item):
        new_node = Node(item)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        print("Insertion success!!!")

    def InsertEnd(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        print("Insertion success!!!")

    def InsertSpecified(self, item, location):
        if not self.head:
            self.InsertBegining(item)
            return
        temp = self.head
        while temp and temp.data != location:
            temp = temp.next
        if not temp:
            print("Given node is not found in the list!!!")
            return
        new_node = Node(item)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        print("Insertion success!!!")

    def DeleteStart(self):
        if not self.head:
            print("List is Empty!!! Deletion not possible!!!")
            return
        temp = self.head
        self.head = temp.next
        if self.head:
            self.head.prev = None
        del temp
        print("Deletion success!!!")

    def DeleteEnd(self):
        if not self.head:
            print("List is Empty!!! Deletion not possible!!!")
            return
        temp = self.head
        if not temp.next:
            self.head = None
        else:
            while temp.next:
                temp = temp.next
            temp.prev.next = None
        del temp
        print("Deletion success!!!")

    def DeleteSpecified(self, item):
        if not self.head:
            print("List is Empty!!! Deletion not possible!!!")
            return
        temp = self.head
        while temp and temp.data != item:
            temp = temp.next
        if not temp:
            print("Given node is not found in the list!!!")
            return
        if temp == self.head:
            self.head = temp.next
            if self.head:
                self.head.prev = None
        else:
            if temp.next:
                temp.next.prev = temp.prev
            temp.prev.next = temp.next
        del temp
        print("Deletion success!!!")

    def traverse(self):
        if not self.head:
            print("List is Empty!!!")
            return
        print("NULL <--- ", end="")
        temp = self.head
        while temp.next:
            print(f"{temp.data} <===> ", end="")
            temp = temp.next
        print(f"{temp.data} ---> NULL")

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            current_node.prev = next_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        print("List reversed!!!")

    def search(self, item):
        temp = self.head
        found = False
        while temp:
            if temp.data == item:
                found = True
                break
            temp = temp.next
        if found:
            print(f"{item} found in the list!!!")
        else:
            print(f"{item} not found in the list!!!")

dll = DoublyLinkedList()

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
                dll.InsertBegining(item)
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
        dll.reverse()
    elif choice1 == '5':
        item = int(input("Enter item to search: "))
        dll.search(item)
    elif choice1 == '6':
        break