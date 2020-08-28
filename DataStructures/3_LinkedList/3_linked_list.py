class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()
#######################################
# code with comments
class Node:
    """Represent elements in linked list"""

    # function to initialize the node object
    def __init__(self, data=None, next=None):
        """Create a node object"""
        # data can contain integer, number or complex object
        self.data = data
        # pointer to next element
        self.next = next


class LinkedList:
    """Represent linked list"""

    def __init__(self):
        """Create a linked list object """
        # head varibale points to the head of linked list
        self.head = None

    # taking data value and inserting that at the beginning of linked list
    def insert_at_begining(self, data):
        """Insert medthod at beginning of linked list"""
        node = Node(data, self.head)
        # the head now is node
        self.head = node

    def print(self):
        """Print function"""

        # if the head is blank
        if self.head is None:
            print("Linked list is empty")
            return

        # if the head is not blank, assign head to iterate
        iterate = self.head
        # empty linked list string
        ll_str = ""
        # follow the link in linked list and iterate one by one
        while iterate:
            # append data the linked list string
            ll_str += str(iterate.data) + '--->'
            iterate = iterate.next

        print(ll_str)

    def insert_at_end(self, data):
        """Insert method at the end of linked list"""
        # if the head is blank
        if self.head is None:
            # the head would be created with data, None means the next one is none
            self.head = Node(data, None)
            return

        # if the linked list is not blank
        # iterate the linked list to the end and insert the element
        iterate = self.head
        # if iterate.next has some value it means we are not at the end of linked list
        while iterate.next:
            # keep on itertating
            iterate = iterate.next
        # when iterate.net becomes null, we are at the last element
        #  new node
        iterate.next = Node(data, None)

    def insert_values(self, data_list):
        """Return new linked list with a list of data"""
        # binding all current values and inserting new values
        # blank head
        self.head = None
        for data in data_list:
            # utilize insert_at_end function
            self.insert_at_end(data)

    def get_length(self):
        """Return length of the linked list"""
        # counter
        count = 0
        # if the head is not blank, assign head to iterate
        iterate = self.head
        while iterate:
            count += 1
            # keep on itertating
            iterate = iterate.next
        return count

    def remove_at_index(self, index):
        """Remove element at index x of linked list"""
        # validate the index, index >= self.get_length() bigger or equal because index starts at 0
        if index < 0 or index >= self.get_length():
            # the raise keyword is used to raise an exception.
            raise Exception("Invalid index")
        # what if we want to remove the head of linked list
        # remove the element at beginning of linke list which is the head
        if index == 0:
            # pointing to next element
            self.head = self.head.next

        # we are removing the index so we have to maintain the count manually to reach that particular index
        count = 0
        # if the head is not blank, assign head to iterate
        iterate = self.head
        while iterate:
            # in linked list we have to stop at the element prior to the gonna be removed element, at that element we can modify the connecting links that we have
            # the link are 1-->2-->3 will be 1-->3
            # that will automatically remove the target element
            # if we want to remove index[2], we start at index[1]
            if count == index-1:
                # tricky part
                iterate.next = iterate.next.next
                # break out of the loop when we archive that
                break

            iterate = iterate.next
            count += 1

    def insert_at_index(self, index, data):
        """Insert element at index x of linked list"""

        # validate the index, index >= self.get_length() bigger or equal because index starts at 0
        if index < 0 or index >= self.get_length():
            # the raise keyword is used to raise an exception.
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_begining(data)
            return data

        count = 0
        # if the head is not blank, assign head to iterate
        iterate = self.head
        while iterate:
            if count == index-1:
                # create a node
                node = Node(data, iterate.next)
                iterate.next = node
                break

            iterate = iterate.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        """Insert element after particular value in linked list"""
        # Search for first occurance of data_after value in linked list
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        # Now insert data_to_insert after data_after node
        iterate = self.head
        while iterate:
            if iterate.data == data_after:
                iterate.next = Node(data_to_insert, iterate.next)
                break
            iterate = iterate.next

    def remove_by_value(self, data):
        """Remove element after particular value in linked list"""
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        # Remove first node that contains data
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


linked_list = LinkedList()
linked_list.insert_at_begining(5)
linked_list.insert_at_begining(85)
linked_list.insert_at_end(45)
linked_list.insert_values(
    ['spider man', 'thor', 'hulk', 'iron man', 'captain american'])
# linked_list.remove_at_index(2)
linked_list.insert_at_index(2, 'wonder woman')
linked_list.insert_after_value('wonder woman', 'hawk eye')
print(linked_list.get_length())
linked_list.print()
linked_list.remove_by_value('spider man')
linked_list.print()
linked_list.remove_by_value('thor')
linked_list.remove_by_value('hulk')
linked_list.remove_by_value('hawk eye')

linked_list.print()
