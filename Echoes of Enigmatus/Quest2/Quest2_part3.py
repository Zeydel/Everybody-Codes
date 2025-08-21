# Function to parse the input
def parse(notes):
    
    operations = []
    
    for line in notes:
        
        words = line.split(' ')
        
        if words[0] == 'ADD':
        
            op_id = words[1].split('=')[1]
            
            left_rank = int(words[2].split('[')[1].split(',')[0])
            
            left_symbol = words[2].split(',')[1].split(']')[0]
            
            left = (left_rank, left_symbol)
            
            right_rank = int(words[3].split('[')[1].split(',')[0])
            
            right_symbol = words[3].split(',')[1].split(']')[0]
    
            right = (right_rank, right_symbol)
            
            operations.append((words[0], op_id, left, right))
        
        elif words[0] == 'SWAP':
            
            op_id = words[1]
            
            operations.append((words[0], op_id))
        
    return operations

class Node:
    
    def __init__(self, op_id, rank, symbol):
        self.op_id = op_id
        self.rank = rank
        self.symbol = symbol
        self.left = None
        self.right = None

# Add a node to a tree
def add(root, op_id, rank, symbol):
    
    # Init new node
    node = Node(op_id, rank, symbol)
    
    # If tree is empty, add as root
    if root == None:
        return node
    
    # Otherwise find out where it should go
    current = root
    
    while True:
                
        # If rank is smaller, go left
        if rank < current.rank:
            
            # If empty spot, put the node here
            if current.left == None:
                current.left = node
                return root
            
            # Otherwise go left
            current = current.left
            continue
        else:
            
            if current.right == None:
                current.right = node
                return root
            
            # Same, but for the right
            current = current.right
            continue    
   
def find_parents(root, op_id):
    
    if root == None:
        return []
    
    nodes = []
    
    if root.left != None and root.left.op_id == op_id:
        nodes.append((root, root.left, 'L'))
    if root.right != None and root.right.op_id == op_id:
        nodes.append((root, root.right, 'R'))
        
    nodes += find_parents(root.left, op_id)
    nodes += find_parents(root.right, op_id)
    
    return nodes
       
def remove_node(root, op_id):
    
    if root == None:
        return root, None
    
    removed = None
    
    if root.left.op_id == op_id:
        removed = root.left
        root.left = None
        return root, removed
        
    if root.right.op_id == op_id:
        removed = root.left
        

# Command to swap two nodes
def swap(left, right, op_id):
          
    # Make a big tree of both trees
    root = Node('', '', '')
    root.left = left
    root.right = right
    
    # Find parents and nodes
    parent1, parent2 = find_parents(root, op_id)

    # Split into value
    p1, n1, p1_node_dir = parent1

    p2, n2, p2_node_dir = parent2
    
    # Replace
    if p1_node_dir == 'L':
        p1.left = n2
    else:
        p1.right = n2
        
    if p2_node_dir == 'L':
        p2.left = n1
    else:
        p2.right = n1
    
    # Return individual subtrees
    return root.left, root.right

# Recursivily get the number of nodes at each level
def get_level_populations(root, level=0):    

    populations = dict()
    
    if root == None:
        return populations

    if level not in populations:
        populations[level] = 1
        
    left_subtree_levels = get_level_populations(root.left, level+1)
        
    for l_populations in left_subtree_levels:
        
        if l_populations not in populations:
            populations[l_populations] = 0
        
        populations[l_populations] += left_subtree_levels[l_populations]
        
    right_subtree_levels = get_level_populations(root.right, level+1)
        
    for r_populations in right_subtree_levels:
        
        if r_populations not in populations:
            populations[r_populations] = 0
        
        populations[r_populations] += right_subtree_levels[r_populations]
    
    return populations
        
# Recurse through tree and read keyword given a level
def read_keyword(root, level, current_level = 0):
            
    if current_level == level:
        return root.symbol
    
    word = ''
    
    if root.left != None:
        word += read_keyword(root.left, level, current_level+1)
        
    if root.right != None:
        word += read_keyword(root.right, level, current_level+1)
        
    return word

# Open and parse input
file = open('input_part3.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
operations = parse(notes)

# Init two trees
left = None
right = None

# Perform all operations on both trees
for operation in operations:
    
    # Get the operation to perform
    op = operation[0]
    
    # Perform the operation
    if op == 'ADD':
        
        op, op_id, left_node, right_node = operation
        
        left = add(left, op_id, left_node[0], left_node[1])
        right = add(right, op_id, right_node[0], right_node[1])
        
    elif op == 'SWAP':
        
        op, op_id = operation
        
        left, right = swap(left, right, op_id)

# Get the keyword
keyword = ''

# For both trees, get most populated level and add read keyword
for tree in [left, right]:

    levels = get_level_populations(tree)

    # Find the most populated level
    most_populated_level = -1
    most_nodes = -1

    for level in levels:
        
        if levels[level] > most_nodes:
            most_nodes = levels[level]
            most_populated_level = level
            
    keyword += read_keyword(tree, most_populated_level)
        
# Print the results
print(f'The keyword is {keyword}')