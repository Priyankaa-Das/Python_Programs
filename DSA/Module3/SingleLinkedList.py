'''Implement Single Linked List in python using the following informations:
Create class node with the members data and next. 
Develop a class Linkedlist with the following members:
Data member start
Define function __init__() to initialize the object of class LinkedList
Define a function InsertBegining() to insert a new node in the beginning of the linked list
Define a function InsertEnd() to insert at the end of the linked list
Define a function InsertSpecified() to insert at specified position
Define a function DeleteStart() to delete the start node
Define a function DeleteEnd() to delete from the end.
Define a function DeleteSpecified() to delete specified node
Define a function traverse() to display all the data of the linked list.
Define a function Reverse() to reverse the order of the nodes in the linked list
Define a function Search() to search an element of the linked list'''

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.start = None

    def InsertBeginning(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            new_node.next = self.start
            self.start = new_node
        print("\nNode inserted at the beginning of the linked list.")

    def InsertEnd(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print("\nNode inserted at the end of the linked list.")

    def InsertSpecified(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.start
            self.start = new_node
        else:
            temp = self.start
            for _ in range(position - 1):
                if temp.next is None:
                    print("\nPosition out of range.")
                    return
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        print("\nNode inserted at specified position.")

    def DeleteStart(self):
        if self.start is None:
            print("\nLinked list is empty.")
        else:
            self.start = self.start.next
            print("\nNode deleted from the start of the linked list.")

    def DeleteEnd(self):
        if self.start is None:
            print("\nLinked list is empty.")
        elif self.start.next is None:
            self.start = None
            print("\nNode deleted from the end of the linked list.")
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            print("\nNode deleted from the end of the linked list.")

    def DeleteSpecified(self, position):
        if position == 0:
            self.start = self.start.next
        else:
            temp = self.start
            for _ in range(position - 1):
                if temp.next is None:
                    print("\nPosition out of range.")
                    return
                temp = temp.next
            if temp.next is None:
                print("\nPosition out of range.")
            else:
                temp.next = temp.next.next
        print("\nNode deleted from specified position.")

    def traverse(self):
        if self.start is None:
            print("\nLinked list is empty.")
        else:
            temp = self.start
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def Reverse(self):
        prev = None
        current = self.start
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.start = prev
        print("\nLinked list reversed.")

    def Search(self, data):
        temp = self.start
        found = False
        while temp is not None:
            if temp.data == data:
                found = True
                break
            temp = temp.next
        if found:
            print("\nElement found in the linked list.")
        else:
            print("\nElement not found in the linked list.")

ll = LinkedList()
while True:
    print("\n1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at specified position")
    print("4. Delete from start")
    print("5. Delete from end")
    print("6. Delete from specified position")
    print("7. Traverse")
    print("8. Reverse")
    print("9. Search")
    print("10. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to insert: "))
        ll.InsertBeginning(data)
    elif choice == 2:
        data = int(input("Enter data to insert: "))
        ll.InsertEnd(data)
    elif choice == 3:
        data = int(input("Enter data to insert: "))
        position = int(input("Enter position to insert: "))
        ll.InsertSpecified(data, position)
    elif choice == 4:
        ll.DeleteStart()
    elif choice == 5:
        ll.DeleteEnd()
    elif choice == 6:
        position = int(input("Enter position to delete: "))
        ll.DeleteSpecified(position)
    elif choice == 7:
        ll.traverse()
    elif choice == 8:
        ll.Reverse()
    elif choice == 9:
        data = int(input("Enter data to search: "))
        ll.Search(data)
    elif choice == 10:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

    print()