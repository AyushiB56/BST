#iteration
def bfs(root):
    current_node=root
    queue=[current_node]
    list_elements=[]
    while len(queue) > 0:
        current_node=queue.pop(0)
        list_elements.append(current_node.value)


        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    return list_elements


#recursion
def bfs(queue, list_elements):
   if len(queue)==0:
          return list_elements
    current_node=queue.pop(0)
    list_elements.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
       
    return bfs(queue,list_elements)




