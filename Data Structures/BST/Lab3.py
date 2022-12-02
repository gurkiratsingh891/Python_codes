def getStudentNumber():
    # This method must return your name EXACTLY as D2L presents it.
    # If this does not work, you will fail this lab.
    return "500689794"


class MyBST:
    def __init__(self, data, promote_right=True):
        # Initialize this node, and store data in it
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

        # Set promote_right to TRUE if you are implementing
        # the promotion of the smallest node on left subtree,
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
        # Return the value of the largest node

    def remove(self, data):
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
        return self
        # Remove find the data in the input parameter and remove it
        # Ensure that the tree remains a valid Binary Search Tree
        # Return this node after data has been inserted

# Bonus functions to help you debug
def printTree_(tree, prefix):
    if tree.getLeft() is not None:
        printTree_(tree.getLeft(), prefix + "+ ")
    print(f"{prefix}{tree.data}")
    if tree.getRight() is not None:
        printTree_(tree.getRight(), prefix + "- ")

def printTree(tree):
    printTree_(tree, "")

if __name__=="__main__":
    #Implement your testing logic here.
    #This code will not execute if this file is loadsed as a library.
    pass

root = MyBST(10)
root = root.insert(20)
#root.insert(30)
#root.insert(40)
root = root.insert(50)
printTree(root)