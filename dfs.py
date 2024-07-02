import collections

class Node:
    def __init__(self, index, left, right):
        self.index = index
        self.right = right
        self.left = left

def DFSRecurssionPreorder(tree):
    if tree:
        print(tree.index)
        DFSRecurssionPreorder(tree.left)
        DFSRecurssionPreorder(tree.right)

def DFSRecurssionInorder(tree):
    if tree:
        DFSRecurssionInorder(tree.left)
        print(tree.index)
        DFSRecurssionInorder(tree.right)

def DFSRecurssionPostorder(tree):
    if tree:
        DFSRecurssionPostorder(tree.left)
        DFSRecurssionPostorder(tree.right)
        print(tree.index)

def DFSIterativePreorder(tree):
    stack = []

    if tree:
        stack.append(tree)

        while stack:
            node = stack.pop()
            if node:
                print(node.index)
                stack.append(node.right)
                stack.append(node.left)
    
def DFSIterativeInorder(tree):
    stack = []

    if tree:
        current = tree

        while current or stack:
            if current:
                stack.append(current)
                current = current.left

            else:
                current = stack.pop()
                print(current.index)
                current = current.right

def DFSIterativePostorder(root):
    # output: "2,3,1"
    stack = []
    printed = collections.defaultdict(bool)

    if not root:
        return
    
    current = root
    stack.insert(0, root)                                                           [1]
	
    while current or stack:
        if current.right and not printed[current.right.index]:
            stack.insert(0, current.right)		                                    [3,1]
        if current.left and not printed[current.left.index]:
            stack.insert(0, current.left)
        else: 
            print(current.index)
            printed[current.index] = True           		                        [3,1] {2}
        current = stack.pop

    #if root:
    #    stack1 = [root]
    #    stack2 = [root]
#
    #    while stack1:
    #        current = stack1.pop()
    #        if current.left:
    #            stack2.append(current.left)
    #            stack1.append(current.left)
    #        elif current.right:
    #            stack2.append(current.right)
    #            stack1.append(current.right)
    #        
    #    while stack2:
    #        node = stack2.pop()
    #        print(node.index)


node4 = Node(4, None, None)
node2 = Node(2, node4, None)
node3 = Node(3, None, None)
root = Node(1, node2, node3)

DFSRecurssionPreorder(root)
print("\n")
DFSRecurssionInorder(root)
print("\n")
DFSRecurssionPostorder(root)
print("\n")
DFSIterativePreorder(root)
print("\n")
DFSIterativeInorder(root)
print("\n")
DFSIterativePostorder(root)
