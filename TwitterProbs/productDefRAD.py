# from stack import Stack

class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left;
        self.right = right;
        self.val = val;

n = Node(3, Node(9, Node(4), Node(98)), Node(23, Node(16)))

def dfs(val, tree):
    # returns the node if found, otherwise None
    stack = []
    stack.append(tree)
    while len(stack) != 0:
        currNode = stack.pop()
        if currNode.val == val:
            return currNode
        if currNode.left:
            stack.append(currNode.left)
        if currNode.right:
            stack.append(currNode.right)    
    return None

    # print(stack)

print(n)
print(dfs(98, n).val)