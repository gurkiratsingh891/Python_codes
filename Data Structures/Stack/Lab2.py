
def getStudentNumber():
    # This method must return a string of your student number
    # If the number does not match your actual student number
    # You will not get the marks for this lab
	return "500689794"


class Node:
    def __init__(self, data, node=None):
        # Initialize this node, insert data, and set the chain node if any
        self.data = data
        self.chain = node

class MyStack:
    def __init__(self, data=None):
        # Initialize this stack, and store data if it exists
        self.head = Node("head")
        self.size = 0
        if data is not None:
            self.push(data)

    def push(self, data):
        # Add data to the beginning of the stack
        node = Node(data)
        node.chain = self.head.chain
        self.head.chain = node
        self.size += 1

    def pop(self):
        # Remove the element at the beginning of the stack.
        # Return the data in the element at the beginning of the stack, or None if the stack is empty
        if self.isEmpty():
            return None
        remove = self.head.chain
        self.head.chain = self.head.chain.chain
        self.size -= 1
        return remove.data

    def top(self):
        # Return the data in the element at the beginning but does not remove it.
        # Return None if stack is empty.
        if self.isEmpty():
            return None
        return self.head.chain.data

    def __len__(self):
        # Return the number of elements in the stack
        return self.size

    def isEmpty(self):
        return self.size == 0

def sum_exists(n, p_list):
    # Returns True if n can be formed from p_list repeated
    # some arbitrary number of times.
    stack = MyStack()
    stack.push(0)
    size = len(p_list)
    i = 0
    while i<size:
        stack1 = MyStack()
        while len(stack) != 0:
            if n%p_list[i] == 0:
                return True
            last = stack.pop()
            if (n - last) % p_list[i] == 0:
                return True
            while last + p_list[i] < n:
                stack1.push(last+p_list[i])
                last = last + p_list[i]
        stack = stack1
        i+=1
    return False
