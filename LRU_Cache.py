class DoubleNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LRU_Cache(object):
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.dict = dict()
        self.capacity = capacity

    def set(self, key, value):
        node = DoubleNode(key, value)
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.dict[key] = node
            self.capacity -= 1
            return

        if self.capacity == 0:
            self.dict.pop(self.head.key)
            self.head = self.head.next
            self.capacity += 1

        self.tail.next = node
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        self.dict[key] = node
        self.capacity -= 1
        return

    def get(self, key):

        if key not in self.dict:
            return -1

        node = self.dict[key]
        #if node is head
        if self.head == node:
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        if node.previous is not None:
            node.previous.next = node.next
        self.capacity += 1
        self.set(node.key, node.value)
        return node.value



our_cache = LRU_Cache(5)
# Test 1
our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))      # return -1

print("Last Value in cache: ", our_cache.tail.key, ":", our_cache.tail.value)  # tail is 2:2 because this key was
# Test 2                                                                       # accessed last
print("\n")
print("Setting some more key-value in cache\n")
our_cache.set(3, None)
our_cache.set(4, "hello")  #last element

print("Last Value in cache: ", our_cache.tail.key, ":", our_cache.tail.value)  # tail is 4 :"hello" because this key was
                                                                               # accessed last
#Test 3
our_cache.set(5, 15)
our_cache.set(5, 16)    #going over capacity should remove oldest node
print(our_cache.get(1)) # returns -1 because first value was removed when capacity was reached
print("Last Value in cache: ", our_cache.tail.key, ":", our_cache.tail.value)  # Last Value in cache:  5 : 16
print("First Value in cache: ", our_cache.head.key, ":", our_cache.head.value) # head is 2 : 2 as oldest now
print(our_cache.get(None))       # no key with None found should print -1



