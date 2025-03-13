#recursion
def dfs_re(stack, list_element):
    if len(stack) == 0:
        return list_element

    currentnode=stack.pop()
    list_element.append(currentnode.value)
    if currentnode.right  is not None:
        stack.append(currentnode.right)
    if currentnode.left is not None:
        stack.append(currentnode.left)
    return dfs_re(stack,list_element)
