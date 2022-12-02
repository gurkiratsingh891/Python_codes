
import time
import math
import random
#Module Imports
import sys
from importlib import import_module

def prepare():
    return True

def CheckHeight(tree):
    if tree is None:
        return -1
    else:
        return max(CheckHeight(tree.getLeft())+1,CheckHeight(tree.getRight())+1)

def CheckBST(tree):
    flag = True
    if tree.getLeft() is not None:
        if tree.getData() <= tree.getLeft().getData():
            return False
        else:
            flag = flag and CheckBST(tree.getLeft())
    if tree.getRight() is not None:
        if tree.getData() > tree.getRight().getData():
            return False
        else:
            flag = flag and CheckBST(tree.getRight())
    return flag
    

def printTree_(tree, prefix):
    if tree.getLeft() is not None:
        printTree_(tree.getLeft(),prefix+"+ ")
    print(f"{prefix}{tree.data}")
    if tree.getRight() is not None:
        printTree_(tree.getRight(),prefix+"- ")

def printTree(tree):
    printTree_(tree,"")

def Test(lib, seed=0, size=10, rounds=10, verbose=False):
    random.seed(a=seed)
    # Test MyTree
    flag = True
    n = random.randint(0, size)
    
    flag = True
    m = size*3
    n = random.randint(size, size*2)

    try:
        bst = lib.MyBST(n)
        for i in range(1,5):
            bst.insert(n+i)
        bst = bst.insert(n-2)
        bst = bst.insert(n-1)
        if bst.getHeight() != 4 or bst.getHeight() != CheckHeight(bst):
            if verbose:
                print("Error: BST height incorrect.")
            flag = False

    except:
        if verbose:
            print("Error: MyBST not creatable")
        flag = False

    
    if verbose:
        if flag:
            print("BST getHeight() test complete.")
        else:
            print("BST getHeight() test failed.")

    try:
        del(bst)
    except:
        pass
    yield flag

    flag = True
    bst= lib.MyBST(n)
    a = [n]
    a_all = [n]
    for i in range(size):
        v = random.randint(0,m)
        bst= bst.insert(v)
        a_all.append(v)
        if not(v in a):
            a.append(v)
        
    for i in range(size):
        if len(a) >= size:
            m*=2
        v = random.randint(0,m)
        if (v in a) != (v in bst):
            if verbose:
                print("Error: BST Search incorrect")
            flag = False
    if verbose:
        if flag:
            print("BST search test complete.")
        else:
            print("BST search test failed.")
    yield flag

    flag = True
    # copy Small/Large test
    minVal = min(a)
    maxVal = max(a)

    try:
        minTree = bst.findSmallest()
        if minVal != minTree:
            verbose and print(f"Error: BST returns minimum value as {minTree} when it should be {minVal}.")
            flag = False
    except:
        verbose and print("Error: findSmallest() does not work.")
        flag = False

    try:
        maxTree = bst.findLargest()
        if maxVal != maxTree:
            verbose and print(f"Error: BST returns minimum value as {maxTree} when it should be {maxVal}.")
            flag = False
    except:
        verbose and print("Error: findLargest() does not work.")
        flag = False


    if flag:
        verbose and print("BST findSmallest and findLargest test complete.")
    else:
        verbose and print("BST findSmallest and findLargest test failed.")   
    yield flag    

    flag = True
    #Remove test
    #tiny
    smol_bst = lib.MyBST(4)
    smol_bst = smol_bst.insert(2)
    smol_bst = smol_bst.insert(3)
    smol_bst = smol_bst.insert(6)
    smol_bst = smol_bst.insert(5)
    try:
        if smol_bst.getHeight() != 2:
            flag = False
        else:
            smol_bst = smol_bst.remove(4)
            if (smol_bst.promote_right and smol_bst.data != 5) or ((not smol_bst.promote_right) and smol_bst.data != 3):
                verbose and print("Error: Remove promoting incorrect value.")
                flag = False
            else:
                if not CheckBST(smol_bst):
                    verbose and print("Error: Tree no longer a BST after removal.")
                    flag = False
            
    except:
        verbose and print("Error: BST Remove non-functional")
        flag = False
    #tiny complete
    del(smol_bst)

    if flag:
        verbose and print("BST Small Removal test complete.")
    else:
        verbose and print("BST Small Removal test failed.")

    yield flag

    if flag:
        try:
            random.shuffle(a)
            d = []
            for v in a:
                for i in range(a_all.count(v)):
                    d.append(v)
            v = d[0]
            for val in d[:-1]:
                bst = bst.remove(val)
                if val != v:
                    if v in bst:
                        verbose and print(f"Error: BST Removal not removing values. {v} still in tree after removing all instances.")
                        flag = False
                    v = val            
            if bst.getData() != d[-1]:
                verbose and print("Error: BST removal not promoting correct values.")
                flag = False
        

        except:
            verbose and print("Error: large BST removal uncompletable.")
            flag = False

        if flag:
            verbose and print("BST Large Removal test complete.")
        else:        
            verbose and print("BST Large Removal test failed.")
        

    else:
        verbose and print("Skipping large BST removal test.")
    yield flag
    
        



    
    
    
if __name__ == "__main__":
    VERBOSE = True 
    if len(sys.argv) < 2:
        name="Lab3"
    else:
        name = sys.argv[1]
        if name.startswith(".\\"):
            name = name[2:]
        if name.endswith(".py"):
            name = name[:-3]
    module=import_module(name,package=__name__)

    prepare()

    print(f"Testing module {name} by {module.getStudentNumber()}")
    score=0
    start = time.time()
    for i in Test(module,seed=987456321, size=20, verbose=VERBOSE):
        if time.time() - start > 10:
            VERBOSE and print("Error: Allowed time elapsed.")
            break
        if i:
            score+=2
        
    if score % 1 == 0:
        score = math.floor(score)
    print(f"Execution time: {round(time.time()-start, 5)} seconds.")
    print(f"Test result: {score}/10")
