# Parse the input into a dictionary of bools
def parse(lines, map_size):
    
    tiles = dict()
    
    max_x = len(lines[0].strip()) // 2
    max_y = len(lines) // 2
    
    for x in range(max_x):
        for y in range(max_y):
            tiles[(x, y)] = lines[y][x] == '#'
            
    return tiles

# The map is symmetrical, so we only need a quater of it
def init_quarter_map(size):
    
    tiles = dict()
    
    for x in range(size//2):
        for y in range(size//2):
            tiles[(x, y)] = False
            
    return tiles
    
# Align targets such that it sits in the lower right part of the map
def align_target(map_size, target_tiles):
    
    max_x, max_y = 0, 0
    
    for x, y in target_tiles:
        
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
            
    offset_x = ((map_size // 2) - max_x) - 1
    offset_y = ((map_size // 2) - max_y) - 1
    
    offset_tiles = dict()
    
    for x, y in target_tiles:
        
        offset_tiles[(x + offset_x, y + offset_y)] = target_tiles[(x, y)]
        
    return offset_tiles
    
    

# Count the number of diagonally adjecent active tiles
def count_active_diagonals(x, y, tiles, map_size):
    
    boundry = (map_size // 2) - 1
    
    neighbors = [(x-1, y-1)]
    
    # Because we are dealing with only a quarter of the map,
    # we need to handle some edge cases. If we are on a border,
    # find neighbors that will exactly correspond to the actual neighbor
    # we need to check
    if x == boundry and y == boundry:
        neighbors.append((x, y))
        neighbors.append((x, y-1))
        neighbors.append((x-1, y))
    elif x == boundry:
        neighbors.append((x-1, y+1))
        neighbors.append((x, y+1))
        neighbors.append((x, y-1))
    elif y == boundry:
        neighbors.append((x+1, y-1))
        neighbors.append((x+1, y))
        neighbors.append((x-1, y))
    else:
        neighbors.append((x+1, y+1))
        neighbors.append((x+1, y-1))
        neighbors.append((x-1, y+1))
        
    active_neighbors = 0
    
    for nx, ny in neighbors:
        
        if (nx, ny) in tiles and tiles[nx, ny]:
            active_neighbors += 1
            
    return active_neighbors

# Get the next iteration of tiles
def get_next_iteration(tiles, map_size):
    
    next_tiles = dict()
    
    # For every tile. calculate the next state
    for tx, ty in tiles:
        
        state = tiles[(tx, ty)]
        
        active_neighbors = count_active_diagonals(tx, ty, tiles, map_size)
        
        if state and active_neighbors % 2 == 1:
            next_tiles[(tx, ty)] = True
        elif not state and active_neighbors % 2 == 0:
            next_tiles[(tx, ty)] = True
        else:
            next_tiles[(tx, ty)] = False
            
    return next_tiles
        
# Count the active tiles
def get_active_count(tiles):
    
    active_tiles = 0
    
    for coords in tiles:
        
        if tiles[coords]:
            active_tiles += 1
            
    return active_tiles

# Get a hash of the map
def get_map_hash(tiles, map_size):
    
    map_hash = ''
    
    for x in range(map_size // 2):
        for y in range(map_size // 2):
            if tiles[(x, y)]:
                map_hash += '#'
            else:
                map_hash += ' '
                
    return map_hash
 
# Check if the map matches the target
def matches_target(tiles, target_tiles):
    
    for coords in target_tiles:
        
        if tiles[coords] != target_tiles[coords]:
            return False
        
    return True

# Get the number of active tiles in a cycle
def get_active_tiles_in_cycles(hashes, remaining_rounds, current_round, current_hash):
    
    # Get cycle start vars
    cycle_start, cycle_start_tiles = hashes[current_hash]
    
    # Get the length of the cycle
    cycle_length = current_round - cycle_start
    
    # Sum up all tiles in the cycle
    cycle_tiles = 0
    
    for h in hashes:
        
        hash_round, tiles = hashes[h]
        
        if hash_round >= cycle_start:
            cycle_tiles += tiles
            
    # Compute how many times we can run the cycle
    cycles = remaining_rounds // cycle_length
    
    # Add the tiles for all cyles to the result
    total_cycle_tiles = cycles * cycle_tiles
        
    # Add the number of cycles times its length to the round
    current_round += cycles * cycle_length
    
    # Return total tiles and current round
    return total_cycle_tiles, current_round
    

# Do a given number of iterations, and keep a running total of tiles       
def count_active_tiles_in_rounds(tiles, target_tiles, map_size, rounds):
    
    # Init total active tiles
    total_active_tiles = 0
    
    # Init set of hashes of maps
    hashes = dict()
    
    # Init round counter
    i = 1
    
    # While there are rounds left to do
    while i <= rounds:
        
        # Perform round
        tiles = get_next_iteration(tiles, map_size)
        
        # If it is a match of the target
        if matches_target(tiles, target_tiles):
        
            # Count active tiles
            active_tiles = get_active_count(tiles)
        
            # Add to total
            total_active_tiles += active_tiles
        
            # Compute hash
            map_hash = get_map_hash(tiles, map_size)
            
            # If we have seen hash before
            if map_hash in hashes:
                
                # It is a cycle, add the tiles for as many cycles as possible
                cycle_tiles, current_round = get_active_tiles_in_cycles(hashes, rounds-i, i, map_hash)
                
                # Add its result to the total
                total_active_tiles += cycle_tiles
                
                # Change i to be the end of every cycle
                i = current_round
                
            # Add hash to dictionary
            hashes[get_map_hash(tiles, map_size)] = (i, active_tiles)
         
        i += 1   
         
    # Return the total active tiles
    return total_active_tiles    

# Read the input as a string
lines = open('input_part3.txt', 'r').readlines()

# Init problem vars
rounds = 1000000000
map_size = 34

# Parse the input
target_tiles = parse(lines, map_size)

# Parse the input
tiles = init_quarter_map(map_size)

# Align target such that the coordinates corresponds to the map
target_tiles = align_target(map_size, target_tiles)

# Get the total number of active tiles in the given number of rounds
# multiply by four because we are only checking a quarter of the map
total_active_tiles = count_active_tiles_in_rounds(tiles, target_tiles, map_size, rounds) * 4

# Print the results
print(f'In total, {total_active_tiles} are active.')