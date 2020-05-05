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
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Choice():
    def __init__(self, move, value):
        self.move = move
        self.value = value

    def __str__(self):
        return self.move + ": " + str(self.value)

class mmBot():
    def __init__(self):
        self.nodes_explored = 0

    def minimax(self, node, is_max):    
        self.nodes_explored = self.nodes_explored + 1

        # base case, if no sub nodes, just return the value
        if (node.left is None and node.right is None):
            return Choice("end", node.value)

        # if node has only one child
        if (node.right is None):
            l_choice = self.minimax(node.left, not is_max)
            return Choice("left", l_choice.value)
        elif (node.left is None):
            r_choice = self.minimax(node.right, not is_max)
            return Choice("right", r_choice.value)

        # if child nodes exist, run minimax on each child nodes
        l_choice = self.minimax(node.left, not is_max)
        r_choice = self.minimax(node.right, not is_max)

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

    def select_move(self, node):
        self.nodes_explored = 0
        return self.minimax(node, True)

class abBot():
    def __init__(self):
        self.nodes_explored = 0

    def minimax(self, node, is_max, alpha, beta):    
        self.nodes_explored = self.nodes_explored + 1

        # base case, if no sub nodes, just return the value
        if (node.left is None and node.right is None):
            return Choice("end", node.value)
        # if node has only one child
        if (node.right is None):
            l_choice = self.minimax(node.left, not is_max, alpha, beta)
            return Choice("left", l_choice.value)
        elif (node.left is None):
            r_choice = self.minimax(node.right, not is_max, alpha, beta)
            return Choice("right", r_choice.value)

        if (is_max):
            # if child nodes exist, run minimax on each child nodes            
            l_choice = self.minimax(node.left, not is_max, alpha, beta)
            alpha = max(l_choice.value, alpha)
            if (alpha >= beta):
                return Choice("left", l_choice.value)
            r_choice = self.minimax(node.right, not is_max, alpha, beta)
            if (l_choice.value > r_choice.value):
                return Choice("left", l_choice.value)
            else:
                return Choice("right", r_choice.value)
        else:
            l_choice = self.minimax(node.left, not is_max, alpha, beta)
            beta = min(l_choice.value, beta)
            if (alpha >= beta):
                return Choice("left", l_choice.value)
            r_choice = self.minimax(node.right, not is_max, alpha, beta)
            if (l_choice.value < r_choice.value):
                return Choice("left", l_choice.value)
            else:
                return Choice("right", r_choice.value)


    def select_move(self, node):
        self.nodes_explored = 0
        return self.minimax(node, True, -1000, 1000)

root = Node("na", 
    Node(3,
        Node(-2,
            Node(20),
            Node(15)),
        Node(4,
            Node(-7),
            Node(7))
    ),
    Node(7,
        Node(9,
            Node(-8),
            Node(-7)),
        Node(99,
            Node(36),
            Node(23))
    )
)

print_tree(root, 4)

one_bot = mmBot()
move = one_bot.select_move(root)
print ("mmBot")
print (move)
print (one_bot.nodes_explored)

two_bot = abBot()
move = two_bot.select_move(root)
print ("\nabBot")
print (move)
print (two_bot.nodes_explored)