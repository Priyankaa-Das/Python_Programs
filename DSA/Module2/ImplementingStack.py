'''Create an ADT for stack using OOPs concept.
Define a class with the name Stack and with the following members:
Data member List l
Data member Size of the array max
Data member top to identify top of the stack
Define a member function(constructor) __init__ () which define an empty list l and define size of the list and initialize top with the value −1.
Define member function Push(), to insert new element at the top of the stack. Modify top value accordingly.
Define member function Traverse() to display all the values of the stack
Define member function Pop() to remove an element from top of the stack.Modify top value accordingly.'''
class Stack:
    def __init__(self,size):
        self.size=size
        self.l=[]
        self.top=-1
        
    def push(self,item):
        if self.top==self.size-1:
            print("Stack overflow")
        else:
            self.top=self.top+1
            self.l.append(item)
    
    def traverse(self):
        print("The items available are: ")
        for i in range(self.top,-1,-1):
            print(self.l[i],end=" ")
            
    def pop(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            item=self.l[self.top]
            self.top=self.top-1
            return item
            
ob=Stack(3)
ob.push(10)
ob.push(20)
ob.push(30)

ob.traverse()
print("\nThe poped elements is: ",ob.pop())
print("\nThe poped elements is: ",ob.pop())
print("\nThe poped elements is: ",ob.pop())
print(ob.pop())