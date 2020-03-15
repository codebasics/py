# Exercise: Linked List

1. In [LinkedList class](https://github.com/codebasics/py/blob/master/DataStructures/3_LinkedList/3_linked_list.py) that we implemented in our tutorial add following two methods,
```
def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

def remove_by_value(self, data):
    # Remove first node that contains data
```
Now make following calls,
```
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
```
[Solution](https://github.com/codebasics/py/blob/master/DataStructures/3_LinkedList/Solution/singly_linked_list_exercise.py)

2. Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. That way you can iterate in forward and backward direction.
Your node class will look this this,
```
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
```
Add following new methods,
```
def print_forward(self):
    # This method prints list in forward direction. Use node.next

def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
```
Implement all other methods in [regular linked list class](https://github.com/codebasics/py/blob/master/DataStructures/3_LinkedList/3_linked_list.py) and make necessary changes for doubly linked list (you need to populate node.prev in all those methods)

[Solution](https://github.com/codebasics/py/blob/master/DataStructures/3_LinkedList/Solution/doubly_linked_list_exercise.py)