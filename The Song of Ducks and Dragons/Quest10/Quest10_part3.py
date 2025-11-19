# Parse the input into a dragon position, a set of sheep positions, a set of
# hideouts, and the x and y bounds of the board
def parse(lines):
    
    dragon = (-1, -1)
    
    sheep = []
    
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
                sheep.append((x, y))
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
def get_next_dragon_positions(position, max_x, max_y):
    
    next_positions = set()
            
    for nx, ny in get_next_positions(position):
            
        if nx < 0 or nx > max_x:
            continue
        if ny < 0 or ny > max_y:
            continue
            
        next_positions.add((nx, ny))
            
    return next_positions

# For every possible position on the board, get every place that a dragon
# can move to
def get_all_next_moves(max_x, max_y):
    
    next_moves = dict()
    
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            
            next_moves[(x,y)] = get_next_dragon_positions((x, y), max_x, max_y)
            
    return next_moves

# Get a hash of the current board state
def get_board_hash(dragon, sheep, depth):
    
    # Take the current search depth
    board_hash = f'{depth}'
    
    # Add the coordinates of the dragon
    board_hash += f'd{dragon[0]},{dragon[1]}'
    
    # And the coordinates of all sheep
    for s in sheep:
        
        board_hash += f's{s[0]},{s[1]}'
        
    return board_hash

# Get the index of every sheep that can move
def get_moveable_sheep(dragon, sheep, hideouts):
    
    # If the dragon is on a hideout, every sheep can move
    if dragon in hideouts:
        return [i for i in range(len(sheep))]
    
    movable_sheep_indices = []
    
    dx, dy = dragon
    
    # For every sheep
    for i, s in enumerate(sheep):
        
        sx, sy = s
        
        # If they would move to the dragon, skip it
        if dx == sx and dy == sy+1:
            continue
        
        # Otherwise add its index to the list
        movable_sheep_indices.append(i)
        
    return movable_sheep_indices
    
# Get all spaces, where a sheep going there would mean that the dragon
# would never be able to catch it
def get_prune_spaces(hideouts, max_x, max_y):
    
    prune_spaces = [(x, max_y+1) for x in range(max_x+1)]

    for x in range(max_x+1):
        
        for y in range(max_y+1, -1, -1):
            
            if (x, y) in hideouts and (x, y+1) in prune_spaces:
                
                prune_spaces = prune_spaces[:x] + [(x, y)] + prune_spaces[x+1:]
    
    return prune_spaces
            
# Get the number of solutions
def get_solutions(dragon, sheep, hideouts, max_x, max_y):
    
    # Init number of solutions as zero
    solutions = 0
    
    # Set of explored states
    explored = set()
    
    # Init search depth
    depth = 0
            
    # Init none state
    none_state = ''
    
    # Create a state dictionary
    states = dict()
    states[none_state] = 1
    
    # Init a state queue, and add the starting state
    queue = []
    queue.append((dragon, sheep, none_state, False, depth))

    # Get all next moves
    next_moves = get_all_next_moves(max_x, max_y)
    
    # Get spaces where a sheep stepping would mean that
    # we prune the search space
    prune_spaces = get_prune_spaces(hideouts, max_x, max_y)
    
    # While there are states left in the queue
    while len(queue) > 0:
        
        # Pop the next state
        dragon, sheep, prev_state, dragons_turn, depth = queue[0]
        queue = queue[1:]
                
        # Get a hash of the board
        board_hash = get_board_hash(dragon, sheep, depth)
        
        # If we have not seen it before, add it the the dict
        if board_hash not in states:
            states[board_hash] = 0
        
        # Add the number of ways to enter the previous states to the
        # number of ways to enter the current state
        states[board_hash] += states[prev_state]
                
        # If we have already seen the board state or there are no more sheep,
        # stop exploring
        if board_hash in explored or len(sheep) == 0:
            continue
        
        # Add board state to explored
        explored.add(board_hash)
        
        # If it is the dragons turn
        if dragons_turn:
            
            # For every move it can make
            for dx, dy in next_moves[(dragon)]:
                
                # If it eats a sheep, remove it from the list
                new_sheep = sheep
                if (dx, dy) in new_sheep and (dx, dy) not in hideouts:
                    
                    i = new_sheep.index((dx, dy))
                    new_sheep = new_sheep[:i] + new_sheep[i+1:]
                
                # If there are now movable sheep, create new states where it
                # is the sheeps turn
                if len(get_moveable_sheep((dx, dy), new_sheep, hideouts)) > 0:
                    queue.append(((dx, dy), new_sheep, board_hash, False, depth + 1))
                
                # Otherwise create new state where it is the dragons turn
                else:
                    queue = [((dx, dy), new_sheep, board_hash, True, depth)] + queue
                    
        # If it is the sheeps turn
        else:
            
            # For every movable sheep
            for i in get_moveable_sheep(dragon, sheep, hideouts):
                
                # Get its position
                sx, sy = sheep[i]
                
                # If it would move into a prune space, continue
                if (sx, sy+1) in prune_spaces:
                    continue
                
                # Create new sheep list
                new_sheep = sheep[:i] + [(sx, sy+1)] + sheep[i+1:]
                
                # Add new state to queue
                queue.append((dragon, new_sheep, board_hash, True, depth + 1))
                
    # For every state
    for state in states:
        
        # If it is a state with no sheep
        if 's' not in state and len(state) > 0:
            
            # Add lists of ways to get there to solution
            solutions += states[state]
                
    # Return number of solutions
    return solutions
    

# Read the input as a string
lines = open('input_part3.txt', 'r').readlines()

# Parse the input
dragon, sheep, hideouts, max_x, max_y = parse(lines)

# Get number of solutions
solutions = get_solutions(dragon, sheep, hideouts, max_x, max_y)

# Print the results
print(f'There are {solutions} ways to eat all the sheep')