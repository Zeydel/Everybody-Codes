# Parse the input into a list of trees
def parse(notes):
    
    trees = []
    
    for line in notes:
        
        trees.append([step for step in line.split(',')])
        
    return trees

# Get the direction in 3D space that each instruction translates to
def get_direction_mappings():
    
    direction_mappings = dict()
    
    direction_mappings['U'] = (1, 0, 0)
    direction_mappings['D'] = (-1, 0, 0)
    
    direction_mappings['L'] = (0, 1, 0)
    direction_mappings['R'] = (0, -1, 0)
    
    direction_mappings['F'] = (0, 0, 1)
    direction_mappings['B'] = (0, 0, -1)
    
    return direction_mappings
    
# Get the 3D coordinates that each tree consists of
def get_tree_nodes(tree):
    
    # Init empty set
    tree_nodes = set()
    
    # Init starting position
    cur_pos = (0, 0, 0)
    
    # Get the direction mappings
    direction_mappings = get_direction_mappings()
    
    # For every step
    for step in tree:
        
        # Split into direction and length
        direction = step[0]
        length = int(step[1:])
        
        # Get the needed direction
        d = direction_mappings[direction]
        
        # For the current length
        for i in range(length):
            
            # Compute new coordinate
            cur_pos = (cur_pos[0] + d[0], cur_pos[1] + d[1], cur_pos[2] + d[2])
            
            # Add it to set
            tree_nodes.add(cur_pos)
            
    # Return set
    return tree_nodes


# Open and parse input
file = open('input_part2.txt','r')
notes = [line.strip() for line in file.readlines()]

# Parse the input
trees = parse(notes)

# Init empty set of nodes
all_tree_nodes = set()

# For every tree, compute set of nodes and add to total set
for tree in trees:

    all_tree_nodes |= get_tree_nodes(tree)
    
# Print the results
print(f"The tree consists of {len(all_tree_nodes)} segments")