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

    # Function to check if the data is present in linked list
    def check_data(self, data):
    
        itr = self.head
        while itr.next:
            if itr.next.data == data or itr.data == data:
                return True
            itr = itr.next

        return False

    # Function to get the length between two index
    # You can also get the length by index2 - index1 + 1
    def get_length_between_index(self, index1, index2):
        count = 0
        result = 0
        itr = self.head

        while itr:
            if count >=index1 and count <= index2:
                result += 1
            itr = itr.next
            count += 1

        return result

    # Function to print the middle element between two indices
    def print_middle_between_index(self, index1, index2):
        if index1 < 0 and index1 >= self.get_length() and index2 < 0 and index2 >= self.get_length():
            raise Exception('Invalid index')

        count = 0
        length = index2 - index1 + 1
        middle = length // 2
        itr = self.head

        while itr:
            if count >= index1 and count < index2:
                self.head = itr
                break
            itr = itr.next
            count += 1

        count = 0    
        itr = self.head
        while itr:
            if count >= index1 and count < index2:
                if count == middle:
                    break
            itr = itr.next
            count += 1

        return itr.data

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()

    print("value between the index is", ll.print_middle_between_index(2, 6))
    ll.print()

    print("Length between the index is",ll.get_length_between_index(0, 4))
    ll.print()

