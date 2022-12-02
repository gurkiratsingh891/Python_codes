
def getStudentNumber():
    return "500689794"


class MyBST():
    def __init__(self, data, promote_right=True):
        # Initialize this node, and store data in it
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

        # Set promote_right to TRUE if you are implementing
        # the promotion of the smallest node on right subtree,
        # Otherwise, set it to FALSE
        self.promote_right = promote_right

    def getLeft(self):
        # Return the left child of this node, or None
        return self.left

    def getRight(self):
        # Return the right child of this node, or None
        return self.right

    def getData(self):
        # Return the data contained in this node
        return self.data

    def getHeight(self):
        # Return the height of this node
        return self.height


    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid Binary Search Tree
        # Return this node after data has been inserted
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = MyBST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = MyBST(data)
        self.updateHeight()
        return self

    # COPY THIS FROM LAB 3
    # OR IMPLEMENT IT HERE IF YOU DID NOT DO LAB 3

    def updateHeight(self):
        # Update the height of this node
        self.height = 0
        if self.left is not None:
            self.left.updateHeight()
            self.height = max(self.height, 1 + self.left.height)
        if self.right is not None:
            self.right.updateHeight()
            self.height = max(self.height, 1 + self.right.height)

    def __contains__(self, data):
        if self.data == data:
            return True
        elif self.data < data:
            if self.right == None:
                return False
            else:
                return self.right.__contains__(data)
        else:
            if self.left == None:
                return False
            else:
                return self.left.__contains__(data)

    def findSmallest(self):
        current = self
        while (current.left is not None):
            current = current.left

        return current.data
        # Return the value of the smallest node

    def findLargest(self):
        current = self
        while (current.right is not None):
            current = current.right

        return current.data

class MyAVL(MyBST):
    def __init__(self, data):
        # Initialize this node, and store data in it
        super().__init__(data)
        self.bf = 0

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid AVL tree
        # Return the node in this node's position after data has been inserted
        if data < self.data:
            if self.left:
                self.left = self.left.insert(data)
            else:
                self.left = MyAVL(data)
        else:
            if self.right:
                self.right = self.right.insert(data)
            else:
                self.right = MyAVL(data)
        self.updateHeight()
        self.bf = self.getBalanceFactor()
        new = self.reBalance()
        return new

    def leftRotate(self):
        # Perform a left rotation on this node and return the new node in its spot
        y = self.right
        z = y.left

        temp = self
        self = y
        self.left = temp
        self.left.right = z
        self.updateHeight()
        return self

    def rightRotate(self):
        # Perform a right rotation on this node and return the new node in its spot
        y = self.left
        z = y.right

        temp = self
        self = y
        self.right = temp
        self.right.left = z
        self.updateHeight()
        return self
    
    def remove(self, data):
        # Remove data from the tree descending from this node and return the new node in its spot
        if self is None:
            return self

        if data < self.data:
            self.left = self.left.remove(data)

        elif (data > self.data):
            self.right = self.right.remove(data)

        else:
            if self.left is None:
                self = self.right
                return self

            elif self.right is None:
                self = self.left
                return self

            succ = self.right
            while succ.left is not None:
                succ = succ.left

            self.right = self.right.remove(succ.data)
            self.data = succ.data

        self.updateHeight()
        self.bf = self.getBalanceFactor()
        new = self.reBalance()
        return new

    def reBalance(self):
        # Apply any rotations needed from this node and return the node in its spot
        if self.bf < -1:
            if self.right.getBalanceFactor() > 0:
                self.right = self.right.rightRotate()
                self = self.leftRotate()
            else:
                self = self.leftRotate()
        elif self.bf > 1:
            if self.left.getBalanceFactor() < 0:
                self.left = self.left.leftRotate()
                self = self.rightRotate()
            else:
                self = self.rightRotate()
        return self

    def getBalanceFactor(self):
        if self is None:
            return 0
        self.bf = 0
        if self.left is not None:
            self.bf = 1 + self.left.getHeight()
        if self.right is not None:
            self.bf = self.bf - (1 + self.right.getHeight())

        return self.bf



def printTree_(tree, prefix):
    if tree.getLeft() is not None:
        printTree_(tree.getLeft(),prefix+"+ ")
    print(f"{prefix}{tree.data}")
    if tree.getRight() is not None:
        printTree_(tree.getRight(),prefix+"- ")

def printTree(tree):
    printTree_(tree,"")

    
# Put any testing code here
# Submit this code with no print statements above this line
if __name__=="__main__":
    pass
