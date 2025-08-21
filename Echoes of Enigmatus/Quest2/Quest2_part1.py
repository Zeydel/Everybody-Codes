# Function to parse the input
def parse(notes):
    
    operations = []
    
    for line in notes:
        
        words = line.split(' ')
        
        op_id = words[1].split('=')[1]
        
        left_rank = int(words[2].split('[')[1].split(',')[0])
        
        left_symbol = words[2].split(',')[1].split(']')[0]
        
        left = (left_rank, left_symbol)
        
        right_rank = int(words[3].split('[')[1].split(',')[0])
        
        right_symbol = words[3].split(',')[1].split(']')[0]

        right = (right_rank, right_symbol)
        
        operations.append((words[0], op_id, left, right))
        
    return operations

# Add a node to a tree
def add(tree, rank, symbol):
    
    # Init new node
    node = (rank, symbol, -1, -1)
    
    # If tree is empty, add as root
    if len(tree) == 0:
        tree['root'] = node
        return tree
    
    # Otherwise find out where it should go
    current = 'root'
    
    while True:
        
        # Get the values of the current node
        c_rank, c_symbol, c_left, c_right = tree[current]
        
        # If rank is smaller, go left
        if rank < c_rank:
            
            # If empty spot, put the node here
            if c_left == -1:
                tree[rank] = node
                tree[current] = (c_rank, c_symbol, rank, c_right)
                return tree
            
            # Otherwise go left
            current = c_left
            continue
        
        # Same, but for the right
        else:
            
            if c_right == -1:
                tree[rank] = node
                tree[current] = (c_rank, c_symbol, c_left, rank)
                return tree
            
            current = c_right
            continue
    
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
def read_keyword(tree, level, current_level = 0, current_node = 'root'):
            
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
file = open('input_part1.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
operations = parse(notes)

# Init two trees
left = dict()
right = dict()

# Perform all operations on both trees
for _, _, left_node, right_node in operations:
    
    left = add(left, left_node[0], left_node[1])
    right = add(right, right_node[0], right_node[1])
    
# Get level population of both trees and
left_populations = get_level_populations(left, 'root')
right_populations = get_level_populations(right, 'root')

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