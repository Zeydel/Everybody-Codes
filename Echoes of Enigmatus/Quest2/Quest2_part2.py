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

# Add a node to a tree
def add(tree, op_id, rank, symbol):
    
    # Init new node
    node = (rank, symbol, -1, -1)
    
    # If tree is empty, add as root
    if len(tree) == 0:
        tree[op_id] = node
        return tree
    
    # Otherwise find out where it should go
    current = '1'
    
    while True:
        
        # Get the values of the current node
        c_rank, c_symbol, c_left, c_right = tree[current]
        
        # If rank is smaller, go left
        if rank < c_rank:
            
            # If empty spot, put the node here
            if c_left == -1:
                tree[op_id] = node
                tree[current] = (c_rank, c_symbol, op_id, c_right)
                return tree
            
            # Otherwise go left
            current = c_left
            continue
        else:
            
            if c_right == -1:
                tree[op_id] = node
                tree[current] = (c_rank, c_symbol, c_left, op_id)
                return tree
            
            # Same, but for the right
            current = c_right
            continue
   
# Command to swap two nodes
def swap(left, right, op_id):
    
    left_rank, left_symbol, left_left, left_right = left[op_id]
    right_rank, right_symbol, right_left, right_right = right[op_id]
    
    left[op_id] = (right_rank, right_symbol, left_left, left_right)
    right[op_id] = (left_rank, left_symbol, right_left, right_right)
    
    return left, right
    
# Recursivily get the number of nodes at each level
def get_level_populations(tree, node, level=0):    

    populations = dict()
    
    if node not in tree:
        return populations

    if level not in populations:
        populations[level] = 1
        
    left_subtree_levels = get_level_populations(tree, tree[node][2], level+1)
        
    for l_populations in left_subtree_levels:
        
        if l_populations not in populations:
            populations[l_populations] = 0
        
        populations[l_populations] += left_subtree_levels[l_populations]
        
    right_subtree_levels = get_level_populations(tree, tree[node][3], level+1)
        
    for r_populations in right_subtree_levels:
        
        if r_populations not in populations:
            populations[r_populations] = 0
        
        populations[r_populations] += right_subtree_levels[r_populations]
    
    return populations
        
# Recurse through tree and read keyword given a level
def read_keyword(tree, level, current_level = 0, current_node = '1'):
            
    if current_level == level:
        return tree[current_node][1]
    
    word = ''
    
    node = tree[current_node]
    
    if node[2] != -1:
        word += read_keyword(tree, level, current_level+1, node[2])
        
    if node[3] != -1:
        word += read_keyword(tree, level, current_level+1, node[3])
        
    return word

# Open and parse input
file = open('input_part2.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
operations = parse(notes)

# Init two trees
left = dict()
right = dict()

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
    
# Get level population of both trees and
left_populations = get_level_populations(left, '1')
right_populations = get_level_populations(right, '1')

levels = set(left_populations.keys())
levels |= set(right_populations.keys())

# Find the most populated level
most_populated_level = -1
most_nodes = -1

for level in levels:
    
    nodes = 0
    
    if level in left_populations:
        nodes += left_populations[level]
        
    if level in right_populations:
        nodes += right_populations[level]
        
    if nodes > most_nodes:
        most_nodes = nodes
        most_populated_level = level
        
# Get the keyword
keyword = ''

keyword += read_keyword(left, most_populated_level)
keyword += read_keyword(right, most_populated_level)

# Print the results
print(f'The keyword is {keyword}')