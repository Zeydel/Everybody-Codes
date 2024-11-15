# Build a tree from the input lines
def build_tree(lines):
    
    # Keep tree as a dict
    tree = dict()
    
    # For every line
    for line in lines:
        
        # Split into vertex name and children
        vertex, children = line.split(':')
        
        # Split children into array
        children = children.split(',')
        
        # Store the key-value pair
        tree[vertex] = children
        
    return tree

# Get paths to fruit
def get_paths_to_fruit(tree, vertex, path = []):
    
    # Init empty list of paths to return
    paths = []
    
    # Create the path to the current vertex
    new_path = path + [vertex]
    
    # If current vertex is a fruit, return the path
    if vertex == '@':
        return [new_path]
    
    # If vertex is a leaf but not a fruit, return an empty result
    if vertex not in tree:
        return []
    
    # For every child, get the paths to fruit
    for c in tree[vertex]:
        paths += get_paths_to_fruit(tree, c, new_path)
            
    # Return the found paths
    return paths
    
    
# Get the path with unique length
def get_path_with_unique_length(paths):
    
    # Store lengths in a dictionary
    lengths = dict()
    
    # For every path
    for path in paths:
        
        # Add its length to the dictionary
        if len(path) not in lengths:
            lengths[len(path)] = 0  
            
        lengths[len(path)] += 1
        
    # Init var for the unique length
    unique_length = -1
        
    # For every length found
    for length in lengths:
        
        # If the length only has one instance
        if lengths[length] == 1:
            
            # Set the unique length
            unique_length = length
            
    # For every path
    for path in paths:
        
        # If the length matches the unique length, return the path
        if len(path) == unique_length:
            return path
        
            
    
# Open file and read lines
file = open('input_part1.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Build the tree
tree = build_tree(lines)

# Init root
root = 'RR'

# Get all paths from root to fruits
paths = get_paths_to_fruit(tree, root)

# Find the path with unique length
unique_length_path = get_path_with_unique_length(paths)

# Convert to string
unique_length_path_string = ''.join(unique_length_path)

# Print the result
print(f'{unique_length_path_string} is the path to the best fruit')