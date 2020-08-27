class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:

    def __init__(self,value = None):
        self.head = None
        self._size = 0
        if value:
            for i in value:
                self.__append__(i)

    def __append__(self,element):
        if self.head == None:
            self.head = Node(element)
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = Node(element)
            pointer2 = pointer.next
            pointer2.previous = pointer
        self._size += 1

    def iter(self):
        return self

    def __len__(self):
        return self._size

    def __str__(self):
        if self.head == None:
            return ''
        string = ''
        for i in range (len(self) -1):
            string += str(self[i])
            string += ','
        string += str(self[len(self) -1])
        return string

    def __repr__(self):
        if self.head == None:
            return 'LinkedList([])'
        string = 'LinkedList(['
        for i in range(len(self) -1):
            string += str(self[i])
            string += ','
        string += str(self[len(self) -1])
        string += '])'
        return string


    def __getitem__(self,index):
        pointer = self.head
        for x in range (index):
            if pointer != None:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer == None:
            raise IndexError("list index out of range")
        else:
            return pointer.value

    def __setitem__(self,index,element):
        pointer = self.head
        for x in range (index):
            if pointer != None:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer == None:
            raise IndexError("list index out of range")
        else:
            pointer.value = element

    def __indice__(self,value):
        pointer = self.head
        if pointer.value == value:
            return 0
        else:
            count = 1
            while pointer != None:
                pointer = pointer.next
                if pointer.value == value:
                    return count
                count += 1
            raise ValueError("LinkedList doesnt have this value")

    def __select__(self,index):
        if index == 0:
            self.head = self.head.next
            self._size -= 1
        pointer = self.head
        for i in range(index):
            pointer = pointer.next
        if pointer == None:
            raise IndexError('LinkedList index out of range')
        else:
            pointer2 = pointer.previous
            pointer3 = pointer.next
            pointer2.next = pointer3
            pointer3.previous = pointer2
            self._size -= 1
            return pointer
    def __insert__(self,index,value):
        if index == 0:
            pointer = self.head
            pointer.previous = Node(value)
            self.head = pointer.previous
            self.head.next = pointer
        else:
            pointer = self.head
            for i in range(index):
                if pointer != None:
                    pointer = pointer.next
                else:
                    raise IndexError('LinkedList index out of range')
            pointer2 = pointer.previous
            pointer3 = Node(value)
            pointer2.next = pointer3
            pointer3.previous = pointer2
            pointer.previous = pointer3
            pointer3.next = pointer

    def __concatenate__(self,self2):
        if self2.head != None:
            pointer = self.head
            for i in range(self._size -1):
                pointer = pointer.next
                if pointer == None:
                    raise IndexError('LinkedList index out of range')
            pointer2 = self2.head
            self._size += self2._size 
            pointer2.previous = pointer
            pointer.next = pointer2
            self2.head = None
            self2.size = 0

class Pointer:
    def __init__(self,linkedList):
        self.linkedList = linkedList
        self.position = self.linkedList.head

    def __next__(self):
        self.position = self.position.next
        if self.position == None:
            raise StopIteration('List has ended')
        return self.position.value
    
    def iter(self):
        return self

class Line(LinkedList):
    
    def __select__(self):
        pointer = self.head
        pointer2 = pointer.next
        self.head = pointer2
        pointer2.previous = None
        self._size -= 1

    def __insert__(self):
        return None

class Stack(LinkedList):

    def __select__(self):
        pointer = self.head
        for i in range(self._size -1):
            pointer = pointer.next
        pointer2 = pointer.previous
        pointer = None
        pointer2.next = None
        self._size -= 1

    def __insert__(self):
        return None

