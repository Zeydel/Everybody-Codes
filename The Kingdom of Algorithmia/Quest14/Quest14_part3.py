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
    
# Get the node coordinates, leaf coordinate and height of a tree
def get_tree_data(tree):
    
    # Init empty set of tree nodes
    tree_nodes = set()
        
    # Init max height
    height = 0
    
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
            
        # If we have exceeded the current max height, save new max
        if cur_pos[0] > height:
            height = cur_pos[0]
                        
    # Return set
    return tree_nodes, cur_pos, height

# Get neighbors of a node
def get_neighbors(node):
    
    neighbors = []
    
    neighbors.append((node[0]+1, node[1], node[2]))
    neighbors.append((node[0]-1, node[1], node[2]))
    
    neighbors.append((node[0], node[1]+1, node[2]))
    neighbors.append((node[0], node[1]-1, node[2]))
    
    neighbors.append((node[0], node[1], node[2]+1))
    neighbors.append((node[0], node[1], node[2]-1))
    
    return neighbors

# Get distance to all leaves from a coordinate
def get_distance_to_leaves(start, leaves, nodes):
    
    # Init distance total and number of leaves found
    distance_sum = 0
    leaves_found = 0
    
    # Init a queue
    queue = [(start, 0)]
    
    # Init empty set of exploaded notes
    explored = set()
    
    while len(queue) > 0:
        
        cur_pos, cur_dist = queue[0]
        queue = queue[1:]
        
        if cur_pos not in nodes or cur_pos in explored:
            continue
        
        if cur_pos in leaves:
            distance_sum += cur_dist
            leaves_found += 1

        if leaves_found == len(leaves):
            return distance_sum

        explored.add(cur_pos)
        
        for neighbor in get_neighbors(cur_pos):
            queue.append((neighbor, cur_dist+1))
    
# Get best murkiness given a tree
def get_best_murkiness(nodes, leaves, max_height):
    
    # In it best as infinite
    best_murkiness = float('inf')
    
    # For every height in the tree
    for height in range(1, max_height+1):
        
        # If node does not exist, continue
        if (height, 0, 0) not in nodes:
            continue
        
        # Compute murkiness
        murkiness = get_distance_to_leaves((height, 0, 0), leaves, nodes)
        
        # If we have beat the record, save new murkiness
        if murkiness < best_murkiness:
            best_murkiness = murkiness
            
    # Return the best murkiness
    return best_murkiness
        
# Open and parse input
file = open('input_part3.txt','r')
notes = [line.strip() for line in file.readlines()]

# Parse the input
trees = parse(notes)

# Init empty set of nodes
all_tree_nodes = set()

leaves = set()

max_height = 0

# For every tree, compute tree data
for tree in trees:

    tree_nodes, leaf, height = get_tree_data(tree)

    all_tree_nodes |= tree_nodes
    
    leaves.add(leaf)
    
    if height > max_height:
        max_height = height
        
# Compute the best murkiness
best_murkiness = get_best_murkiness(all_tree_nodes, leaves, max_height)
    
# Print the results
print(f"The best murkiness possible is {best_murkiness}")