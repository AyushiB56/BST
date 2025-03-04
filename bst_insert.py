class bst:
    def __init__(self,value):
        self.value= value
        self.left = None
        self.right= None

def const(tree_dict):
    new_dict={}
    for nodes in tree_dict["nodes"]:
        new_dict[nodes["id"]]= bst(nodes["value"])



    for nodes in tree_dict["nodes"]:
        if nodes["left"] !="None" :
            new_dict[nodes["id"]].left = new_dict[nodes["left"]]
        if nodes["right"] !="None":
            new_dict[nodes["id"]].right = new_dict[nodes["right"]]
    return new_dict[tree_dict["root"]]




def insert(root, value):
    current_node= root
    while current_node is not None:
        if value < current_node.value:
            if current_node.left is not None:
                current_node= current_node.left
            else:
                current_node.left = bst(value)
                break
        elif value > current_node.value:
            if current_node.right is not None:
                 current_node= current_node.right
            else:
                current_node.right = bst(value)
                break

    return self
