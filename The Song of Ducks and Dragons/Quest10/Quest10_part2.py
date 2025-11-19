# Parse the input into a dragon position, a set of sheep positions, a set of
# hideouts, and the x and y bounds of the board
def parse(lines):
    
    dragon = (-1, -1)
    
    sheep = set()
    
    hideouts = set()
    
    max_x = -1
    
    max_y = len(lines) - 1
    
    for y, line in enumerate(lines):
        
        line = line.strip()
        
        max_x = len(line) - 1
        
        for x, char in enumerate(line):
            
            if char == 'D':
                dragon = (x, y)
            elif char == 'S':
                sheep.add((x, y))
            elif char == '#':
                hideouts.add((x, y))
    
    return dragon, sheep, hideouts, max_x, max_y

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

# For a set of dragon positions, get every next possible
# dragon position within bounds
def get_next_dragon_positions(dragon_positions, max_x, max_y):
    
    next_positions = set()
    
    for pos in dragon_positions:
        
        for nx, ny in get_next_positions(pos):
            
            if nx < 0 or nx > max_x:
                continue
            if ny < 0 or ny > max_y:
                continue
            
            next_positions.add((nx, ny))
            
    return next_positions

# For a set of sheep, get all their next possible positions
# including removing sheep at the end of the board
def get_next_sheep_positions(sheep, max_y):
    
    new_sheep = set()
    
    for sx, sy in sheep:
        
        if sy == max_y:
            continue
        
        new_sheep.add((sx, sy+1))
        
    return new_sheep
    
# Given dragon, sheep and hideout position, perform set operations
# to eat sheep. Return new set of sheep and number of eaten sheep
def eat_sheep(dragon_positions, sheep, hideouts):
    
    unsafe_sheep = sheep - hideouts
            
    eaten_sheep = unsafe_sheep & dragon_positions
                
    sheep -= eaten_sheep
    
    return sheep, len(eaten_sheep)

# BFS to get all positions reachable within a given number of turns
def get_catchable_sheep(dragon, sheep, hideouts, max_x, max_y, max_depth):
    
    # Init queue with starting position
    dragon_positions = set()
    dragon_positions.add(dragon)
    
    # Variable to signal wether it is dragaons or sheeps turn
    dragon_turn = True
    
    # Number of sheep caught
    caught_sheep = 0
    
    # Number of turns played
    turns = 0
    
    # While there are turns to play
    while turns < max_depth:
        
        # If it is the dragons turn
        if dragon_turn:
            
            # Get all next possible dragon positions
            dragon_positions = get_next_dragon_positions(dragon_positions, max_x, max_y)
                        
        # If it is the sheeps turns, get next sheep positions
        else:
            
            sheep = get_next_sheep_positions(sheep, max_y)
                        
            # Increment turn counter
            turns += 1
            
        # Eat sheep
        sheep, eaten_sheep = eat_sheep(dragon_positions, sheep, hideouts)
            
        # Add eaten sheep to solution
        caught_sheep += eaten_sheep
            
        # Flip the turn variable
        dragon_turn = not dragon_turn
            
    # Return positions
    return caught_sheep
                
# Read the input as a string
lines = open('input_part2.txt', 'r').readlines()

# Parse the inpt
dragon, sheep, hideouts, max_x, max_y = parse(lines)

# Init problem variable
max_depth = 20

# Get positions reachable in given number of moves
caught_sheep = get_catchable_sheep(dragon, sheep, hideouts, max_x, max_y, max_depth)

# Print the results
print(f'{caught_sheep} sheep are eatable within {max_depth} turns')