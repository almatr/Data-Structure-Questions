class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def check_for_duplicates(self, other):

        if self.head is None:
            self.head = Node(other.value)
            return

        if self.size() == 1:     #only one node, check if head is same value and return
           if self.head.value == other.value:
               return

        node = self.head
        while node.next:
            if node.value == other.value:
                return
            node = node.next
        node.next = Node(other.value)

    def check_for_intersecting(self, other):

        if self.head is None:
            return

        node = self.head
        while node:
            if node.value == other.value:
                return node
            node = node.next

#check lists for duplicates and merge lists to create union
def union(llist_1, llist_2):

    unionList = LinkedList()
    if llist_1.size() == 0 and llist_2.size() != 0:
        unionList = llist_2
        return unionList
    if llist_1.size() != 0 and llist_2.size() == 0:
        unionList = llist_1
        return unionList

    node = llist_1.head
    while node:
        unionList.check_for_duplicates(node)
        node = node.next

    node = llist_2.head
    while node:
        unionList.check_for_duplicates(node)
        node = node.next

    return unionList

#check lists for duplicates and find intersecting elements in the list
def intersection(llist_1, llist_2):

    interList = LinkedList()     #interList use for appending intersecting elements
    first_list = LinkedList()    #first_list use to create list with no duplicates
    second_list = LinkedList()   #second_list use to create list with no duplicates

    node = llist_1.head
    while node:
        first_list.check_for_duplicates(node)
        node = node.next

    node = llist_2.head
    while node:
        second_list.check_for_duplicates(node)
        node = node.next

    # now that we have no duplicates check for intersecting elements and append to interList
    node = second_list.head
    while node:
        interNode = first_list.check_for_intersecting(node)
        if interNode:
            interList.append(interNode.value)
        node = node.next

    return interList

# Test case 1

print("First test")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(linked_list_1) #3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 ->
print(linked_list_2) #6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 ->

print("Union")
print (union(linked_list_1,linked_list_2))  #3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
print("Intersection")
print (intersection(linked_list_1,linked_list_2)) #6 -> 4 -> 21 ->

# Test case 2
print("Second test")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(linked_list_3)  #3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 ->
print(linked_list_4)  # 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 ->

print("Union")
print (union(linked_list_3,linked_list_4)) #3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print("Intersection")
print (intersection(linked_list_3,linked_list_4)) #should not print anything because of no interesting elements

# Test case 3
print("Third test")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [1]
element_6 = [1,7,8,9,11,21,1]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print(linked_list_5)  #1 ->
print(linked_list_6)  #1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 ->

print("Union")
print (union(linked_list_5,linked_list_6)) #1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print("Intersection")
print (intersection(linked_list_5,linked_list_6)) #1 ->

# Test case 4
print("Fourth test")
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_7 = [1]
element_8 = [1]

for i in element_7:
    linked_list_7.append(i)

for i in element_8:
    linked_list_8.append(i)

print(linked_list_7) #1 ->
print(linked_list_8) #1 ->

print("Union")
print (union(linked_list_7,linked_list_8))  #1 ->
print("Intersection")
print (intersection(linked_list_7,linked_list_8))  #1 ->
