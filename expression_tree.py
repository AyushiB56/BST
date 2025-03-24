# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    current_node= tree
    if current_node.value>=0:
        return current_node.value
    left_value= evaluateExpressionTree(current_node.left)
    right_value= evaluateExpressionTree(current_node.right)
    if current_node.value == -1:
        return left_value + right_value

    if current_node.value == -2:
        return left_value - right_value
    if current_node.value == -3:
        return int(left_value / right_value)

    if current_node.value == -4:
        return left_value * right_value



   
               
               
           
