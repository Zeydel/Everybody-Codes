# Parse the input into a dragon position and a set of sheep positions
def parse(lines):
    
    dragon = (-1, -1)
    
    sheep = set()
    
    for y, line in enumerate(lines):
        
        line = line.strip()
        
        for x, char in enumerate(line):
            
            if char == 'D':
                dragon = (x, y)
            elif char == 'S':
                sheep.add((x, y))
                
    return dragon, sheep

# Get the next position a dragon can move into
def get_next_positions(position):
    
    x, y = position
    
    return [(x+2, y+1),
            (x+2, y-1),
            (x-2, y+1),
            (x-2, y-1),
            (x+1, y+2),
            (x+1, y-2),
            (x-1, y+2),
            (x-1, y-2)]

# BFS to get all positions reachable within a given number of turns
def get_reachable_positions(dragon, max_depth):
    
    # Init queue with starting position
    queue = [(dragon, 0)]
    
    # Init set of position
    positions = set()
    
    # While there are items left in the queue
    while len(queue) > 0:
        
        # Pop the first element
        pos, depth = queue[0]
        queue = queue[1:]
        
        # Add position to set
        positions.add(pos)
        
        # If we have made the maximum number of allowed moves, dont do anything else
        if depth == max_depth:
            continue
        
        # For all the next possible positions
        for next_pos in get_next_positions(pos):
            
            # Add them to queue and increment depth
            queue.append((next_pos, depth+1))
            
    # Return positions
    return positions
                
# Read the input as a string
lines = open('input_part1.txt', 'r').readlines()

# Parse the inpt
dragon, sheep = parse(lines)

# Init problem variable
max_depth = 4

# Get positions reachable in given number of moves
positions = get_reachable_positions(dragon, max_depth)

# Count overlaps between sheep and positions
reachable_sheep = len(sheep & positions)

# Print the results
print(f'{reachable_sheep} are reachable within {max_depth} turns')