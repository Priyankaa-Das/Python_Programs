'''Given the head of a singly linked list, return true if it is a palindrome.
Input: head = [1,2,2,1]
Output: true
Input: head = [1,2]
Output: false
Constraints:
            • The number of nodes in the list is in the range [1, 105].
            • 0 <= Node.val <= 9'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def is_palindrome(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_temp = slow.next
            slow.next = prev
            prev = slow
            slow = next_temp

        left = self.head
        right = prev
        while right:
            if left.value != right.value:
                return False
            left = left.next
            right = right.next

        return True

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("NULL")


ll = LinkedList()
while True:
    print("1. Insertion")
    print("2. Check Palindrome")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = input("Enter value to insert: ")
        ll.insert(val)
    elif choice == 2:
        ll.display()
        print("Is Palindrome?: ", ll.is_palindrome())
    else:
        break 