def get_spacing(depth):
    first_num_spacing = 2 ** depth
    other_num_spacing = 0
    if (depth == 1):
        other_num_spacing = 3
    elif (depth == 2):
        other_num_spacing = 7
    elif (depth == 3):
        other_num_spacing = 15
    elif (depth == 4):
        other_num_spacing = 31
    return [first_num_spacing, other_num_spacing]
    

def print_tree(node, depth):
    layer_nodes = [node]
    while (len(layer_nodes) > 0):
        layer_has_nodes = False
        next_layer_nodes = []
        current_values = []
        spacing = get_spacing(depth)
        first_num_spacing = spacing[0]
        other_num_spacing = spacing[1]
        for i in range(len(layer_nodes)):
            n = layer_nodes[i]
            if (n is not None):
                layer_has_nodes = True
                if (n.left != None):
                    next_layer_nodes.append(n.left)
                else:
                    next_layer_nodes.append(None)
                if (n.right != None):
                    next_layer_nodes.append(n.right)
                else:
                    next_layer_nodes.append(None)
                #make every number two chars long
                svalue = str(n.value).rjust(2, ' ')
            else:
                svalue = '  '
            #spacing for layers
            if (len(current_values) == 0):
                svalue = svalue.rjust(first_num_spacing, ' ')
            else:
                svalue = svalue.rjust(other_num_spacing, ' ')
            current_values.append(svalue)
        if (layer_has_nodes):
            print (' '.join(current_values))
        layer_nodes = next_layer_nodes
        depth = depth - 1

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Choice():
    def __init__(self, move, value):
        self.move = move
        self.value = value

    def __str__(self):
        return self.move + ": " + str(self.value)

def minimax(node, is_max):    
    # base case, if no sub nodes, just return the value
    if (node.left is None and node.right is None):
        return Choice("end", node.value)

    # if node has only one child
    if (node.right is None):
        l_choice = minimax(node.left, not is_max)
        return Choice("left", l_choice.value)
    elif (node.left is None):
        r_choice = minimax(node.right, not is_max)
        return Choice("right", r_choice.value)

    # if child nodes exist, run minimax on each child nodes
    l_choice = minimax(node.left, not is_max)
    r_choice = minimax(node.right, not is_max)

    # compare results
    if (is_max):
        if (l_choice.value > r_choice.value):
            return Choice("left", l_choice.value)
        else:
            return Choice("right", r_choice.value)
    else:
        if (l_choice.value < r_choice.value):
            return Choice("left", l_choice.value)
        else:
            return Choice("right", r_choice.value)

# 4th layer
leaf1 = Node(-8)
leaf2 = Node(7)
leaf3 = Node(15)
leaf4 = Node(14)
leaf5 = Node(8)
leaf6 = Node(-5)
leaf7 = Node(1)
leaf8 = Node(0)

# 3rd layer
body3_1 = Node(3)
body3_1.left = leaf1
body3_1.right = leaf2

body3_2 = Node(20)
body3_2.left = leaf3
body3_2.right = leaf4

body3_3 = Node(-8)
body3_3.left = leaf5
body3_3.right = leaf6

body3_4 = Node(-1)
body3_4.left = leaf7
body3_4.right = leaf8

# 2nd layer
body2_1 = Node(-2)
body2_1.left = body3_1
body2_1.right = body3_2

body2_2 = Node(10)
body2_2.left = body3_3
body2_2.right = body3_4

# root
root = Node(None)
root.left = body2_1
root.right = body2_2
print_tree(root, 4)

print ("\n")
# initialize our state
current_node = root
is_max = True
while (True):
    # run minimax on current node
    choice = minimax(current_node, is_max)
    
    # make choice based on minimax outcome
    if (choice.move == "left"):
        print ("Moving left to node with value " + str(current_node.left.value))
        current_node = current_node.left
    elif (choice.move == "right"):
        print ("Moving right to node with value " + str(current_node.right.value))
        current_node = current_node.right
    elif (choice.move == "end"):
        print ("Game ends with a score of " + str(choice.value))
        break
    # flip players turn
    is_max = not is_max