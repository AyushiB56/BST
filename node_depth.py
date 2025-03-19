#iteration
def nodeDepths(root):
    queue=[(root,0)]
    current_depth=0

    while len(queue)>0:
        current_node,depth= queue.pop(0)
        current_depth+=depth
        if current_node.left:
            queue.append((current_node.left,depth+1))
        if current_node.right:
            queue.append((current_node.right,depth+1))

    return current_depth

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



#recursion
def nodeDepths(root,depth=0):
    cuurent_node=root
    if root is None:
         return 0
    left_depth= nodeDepths(cuurent_node.left,depth+1)
    right_depth=nodeDepths(cuurent_node.right,depth+1)
    return depth+left_depth+right_depth

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
