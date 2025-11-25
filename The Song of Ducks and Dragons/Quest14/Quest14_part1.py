# Parse the input into a dictionary of bools
def parse(lines):
    
    tiles = dict()
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            
            tiles[(x, y)] = char == '#'
            
    return tiles

# Count the number of diagonally adjecent active tiles
def count_active_diagonals(x, y, tiles):
    
    neighbors = [(x+1, y+1),
                 (x+1, y-1),
                 (x-1, y+1),
                 (x-1, y-1)]
    
    active_neighbors = 0
    
    for nx, ny in neighbors:
        
        if (nx, ny) in tiles and tiles[nx, ny]:
            active_neighbors += 1
            
    return active_neighbors

# Get the next iteration of tiles
def get_next_iteration(tiles):
    
    next_tiles = dict()
    
    # For every tile. calculate the next state
    for tx, ty in tiles:
        
        state = tiles[(tx, ty)]
        
        active_neighbors = count_active_diagonals(tx, ty, tiles)
        
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
 
# Do a given number of iterations, and keep a running total of tiles       
def count_active_tiles_in_rounds(tiles, rounds):
    
    total_active_tiles = 0
    
    for i in range(rounds):
        
        tiles = get_next_iteration(tiles)
        
        total_active_tiles += get_active_count(tiles)
                
    return total_active_tiles    

# Read the input as a string
lines = open('input_part1.txt', 'r').readlines()

# Parse the input
tiles = parse(lines)

# Init problem var
rounds = 10

# Get the results
total_active_tiles = count_active_tiles_in_rounds(tiles, rounds)

# Print the results
print(f'In total, {total_active_tiles} are active.')