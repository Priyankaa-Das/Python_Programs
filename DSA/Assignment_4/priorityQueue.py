'''In the lecture, we have introduced priority queues as an abstract data type that supports the operations: 
void insert(int i)
int extractMax().
With insert, one inserts a new value into the queue. 
The method extractMax returns the maximal value currently in the queue and deletes that value from the queue. 
If the queue is empty, it returns a default value or raises an exception, depending on the implementation. 
(In a more general version of priority queues, which we do
not want to implement in this assignment, the method insert would insert an object
one of whose attributes is the key attribute for the queue. 
Similarly, extractMax would return an object with the maximal value and delete that object from the queue.)
One way to realize priority queues, is to use heaps based on arrays. 
The downside is that a queue may become “full” so that no new entries can be inserted. 
In this exercise, you are asked to realize a priority queue with binary trees. 
The implementation is based on two classes, PQueue and PNode. 
A priority queue object has a pointer “root” to an element of class PNode:
class PQueue{ PNode root;}
PNodes themselves are instances of the class PNode defined as follows:
class PNode{ int key; PNode left, right, parent; int lcount, rcount; // Number of nodes in the left // and right subtree}
Using the above data structure, implement priority queues as binary trees that
have the heap property (“for each subtree, the key of the root is greater or equal than all the value in the subtree”.)'''