# Parse the input into a dictionary of barrel locations
def parse(lines):
    
    barrels = dict()
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            barrels[(x, y)] = int(char)
            
    max_y = len(lines)-1
    max_x = len(lines[0].strip())-1
            
    return barrels, max_x, max_y
            
# Get the barrels that are adjecent to a coordinate
def get_adjecent_barrels(x, y):
    
    return [(x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1),]

# Get the barrels that will explode with BFS
def get_exploding_barrels(barrels, x, y):

    # Init set of exploding barrels
    exploding_barrels = set()

    # Define starting barrel
    starting_barrel = (x, y)

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
    return exploding_barrels
        
# Get the needed set of exploding sets
def get_fireball_barrels(barrels, max_x, max_y):
    
    # Set of barrels we have seen explode this far
    exploded_barrels = set()
    
    # Init empty list of exploding barrel set
    explode_sets = []
    
    # For every x and y pair
    for x in range(max_x+1):
        for y in range(max_y+1):
            
            # If we have already seen the barrel explode,
            # exploding it would create a subset of a previous explosion,
            # so we will not need it
            if (x, y) in exploded_barrels:
                continue
            
            # Get the exploding barrels for the coordinate
            coord_barrels = get_exploding_barrels(barrels, x, y)
            
            # Add exploding barrels to set
            exploded_barrels |= coord_barrels
            
            # Add exploding barrels to list
            explode_sets.append(coord_barrels)
    
    # Return the explode sets
    return explode_sets

# Get the best sets
def get_best_set_amounts(explode_sets, set_amount):
            
    # Initially empty set of best barrel explosions
    exploded = set()
    
    # Fireballs shot so far
    fireballs = 0
    
    # While there are fireballs left to shoot
    while fireballs != set_amount:
        
        # Init var to store the next best set
        best_set = set()
        
        # For every set
        for es in explode_sets:
            
            # Get how many barrels we would explode that are not
            # aready exploded
            new_set = es - exploded
            
            # If if is better than the current, save it
            if len(new_set) > len(best_set):
                best_set = new_set
        
        # Add the best set to the set of exploded
        exploded |= best_set
        
        # Increment fireballs
        fireballs += 1
                        
    # Return the size of the exploded set
    return len(exploded)
            

# Read the input as a string
lines = open('input_part3.txt', 'r').readlines()

# Parse the input
barrels, max_x, max_y = parse(lines)

# Get the number of exploding barrels
explode_sets = get_fireball_barrels(barrels, max_x, max_y)

# Get the size of the combined sets of the best three exploded sets
exploded_barrels = get_best_set_amounts(explode_sets, 3)

# Print the results
print(f'The best possible result is {exploded_barrels} exploded barrels')