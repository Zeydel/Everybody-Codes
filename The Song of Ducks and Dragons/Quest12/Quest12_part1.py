# Parse the input into a dictionary of barrel locations
def parse(lines):
    
    barrels = dict()
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            barrels[(x, y)] = int(char)
            
    return barrels
            
# Get the barrels that are adjecent to a coordinate
def get_adjecent_barrels(x, y):
    
    return [(x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1),]

# Get the barrels that will explode with BFS
def get_exploding_barrels(barrels):

    # Init set of exploding barrels
    exploding_barrels = set()

    # Define starting barrel
    starting_barrel = (0, 0)

    # Make a queue and add the starting barrel
    queue = []

    queue.append((starting_barrel, float('inf')))
    
    # While there are barrels left in the queue
    while len(queue) > 0:
        
        # Pop the next barrel
        barrel, prev_size = queue.pop(0)
        
        # If it has already exploded, continue
        if barrel in exploding_barrels:
            continue
            
        # If the barrel is smaller than the previous, continue
        if barrels[barrel] > prev_size:
            continue
        
        # Add barrel to set of exploding barrels
        exploding_barrels.add(barrel)
        
        # For each adjecant barrel
        for nx, ny in get_adjecent_barrels(barrel[0], barrel[1]):
            
            # If it exisits in the dict
            if (nx, ny) in barrels:
                
                # Add it to dictionary
                queue.append(((nx, ny), barrels[barrel]))
                
    # Return the size of the set of barrels
    return len(exploding_barrels)
        


# Read the input as a string
lines = open('input_part1.txt', 'r').readlines()

# Parse the input
barrels = parse(lines)

# Get the number of exploding barrels
exploding_barrels = get_exploding_barrels(barrels)

# Print the results
print(f'The number of exploding barrels is {exploding_barrels}')