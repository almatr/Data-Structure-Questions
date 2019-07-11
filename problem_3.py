import sys

class Node(object):

    def __init__(self, frequency = None, value = None):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None

    def set_left_child(self,node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def is_leaf(self):
        return (not self.has_right_child() and not self.has_left_child())


class HuffmanCode(object):

    def __init__(self, data):
        self.data = data
        self.countList = []
        self.sortedNodes = []
        self.letterToCode = dict()

    def appendNode(self, node):
        count = 0

        for n in self.sortedNodes:
            if n.frequency < node.frequency:
                count +=1
        return count

    def appendtoCount(self):

        for i in self.data:
            self.countList.append((self.data.count(i), i))
        self.countList = set(self.countList)

        if len(self.countList) < 2:
            self.countList.add((0, "\0"))

    def appendToNode(self):

        for i in self.countList:
            node = Node(*i)
            index = self.appendNode(node)
            self.sortedNodes.insert(index,node)

    def createNodesTree(self):

        while len(self.sortedNodes) > 1:
            first_node = self.sortedNodes.pop(0) #pop first node
            sec_node = self.sortedNodes.pop(0)   #pop second node which is now on the index zero because first was popped

            root_frequency = first_node.frequency + sec_node.frequency

            #third_node acting as a root with left and right children
            third_node = Node(root_frequency, None)
            third_node.set_left_child(first_node)
            third_node.set_right_child(sec_node)
            index = self.appendNode(third_node)
            self.sortedNodes.insert(index,third_node)
        return self.sortedNodes[0]

    def createPath(self):

        node = self.createNodesTree()
        encoded = ""

        if not node.is_leaf():
            self.traverseTree(node, encoded)

    def traverseTree(self, node, encoded):

        if node.value != None:
            self.letterToCode[node.value] = encoded
            node.frequency = encoded
            return
        self.traverseTree(node.left, encoded + "0")
        self.traverseTree(node.right, encoded + "1")

    def getBinaryData(self):

        retBinary = ""
        for char in self.data:
            if char in self.letterToCode:
                retBinary = (retBinary + self.letterToCode[char])
        return retBinary

    def fromBinaryToStr(self, encoded_data, node):

        root = node
        retStr = ""
        for i in encoded_data:
            if i == "0":
                root = root.left
            else:
                root = root.right
            if root.is_leaf():
                retStr = retStr + root.value
                root = node
        return retStr


def huffman_encoding(data):

    if len(data) == 0:
        return (None, None)
    huffData = HuffmanCode(data)
    huffData.appendtoCount()
    huffData.appendToNode()
    huffData.createPath()
    root = huffData.sortedNodes[0]
    return huffData.getBinaryData(), root


def huffman_decoding(data,tree):
    if data == 0:
        return None
    if tree == None:
        return None
    huffData = HuffmanCode(data)
    return huffData.fromBinaryToStr(data,tree)


if __name__ == "__main__":
    codes = {}

    #Test case 1
    a_great_sentence = "The bird is the word" #just a normal sentence

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))  #The size of the data is: 69
    print ("The content of the data is: {}\n".format(a_great_sentence))#The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 1111101000110111010110001101100111110010110010100011011000111100001101

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: The bird is the word

    #Test case 2
    a_great_sentence = "T"   #edge case

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    #The size of the data is: 50
    print ("The content of the data is: {}\n".format(a_great_sentence))
    #The content of the data is: T

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #The size of the encoded data is: 28
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 1

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 50
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: T

    #Test case 3

    a_great_sentence = "Here is another sentence, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"   # large number of A's

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    #The size of the data is: 112
    print ("The content of the data is: {}\n".format(a_great_sentence))
    #The content of the data is: Here is another sentence, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #The size of the encoded data is: 48
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 011000001010110010111000110010100111000111010001101100000001000101011011101010
    # 00101000000001010001101000101100101111111111111111111111111111111111111111

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 112
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: Here is another sentence, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    a_great_sentence = ""      #empty data
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    #The size of the data issssss: 49
    print ("The content of the data is: {}\n".format(a_great_sentence))
    #The content of the data is:
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print(encoded_data)  # print None

    decoded_data = huffman_decoding(encoded_data, tree)
    print(decoded_data) # print None

