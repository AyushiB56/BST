def lookup(root, value):
    current_node= root
    print(current_node.value)
    while True:
        if value < current_node.value:
            if current_node.left is not None:
                    current_node= current_node.left
            elif current_node.value==value:
                    return current_node
            else:
                    return "value not found"


        elif value > current_node.value:
                if current_node.right is not None:
                    current_node= current_node.right
                elif current_node.value==value:
                    return current_node
                else:
                    return "value not found"

