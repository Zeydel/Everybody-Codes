# Parse the notes into instructions, letters, and grid dimensions
def parse(notes):
    
    instructions = notes[0]
    
    letters = dict()
    
    for y in range(2, len(notes)):
        for x in range(len(notes[y])):
            letters[(x,y-2)] = notes[y][x]
            
    return instructions, letters, len(notes)-3, len(notes[2])-1
            
# Do a single rotation around a point
def do_rotation(direction, letters, point):
    
    # Identify all neighbors
    x, y = point
    
    neighbors = []
    
    neighbors.append(((x-1, y-1), letters[(x-1, y-1)]))
    neighbors.append(((x, y-1), letters[(x, y-1)]))
    neighbors.append(((x+1, y-1), letters[(x+1, y-1)]))

    neighbors.append(((x+1, y), letters[(x+1, y)]))
    neighbors.append(((x+1, y+1), letters[(x+1, y+1)]))

    neighbors.append(((x, y+1), letters[(x, y+1)]))
    neighbors.append(((x-1, y+1), letters[(x-1, y+1)]))
    
    neighbors.append(((x-1, y), letters[(x-1, y)]))
    
    # Reverse direction if we are going the other way
    if direction == 'L':
        neighbors = neighbors[::-1]
    
    # Substitute each letter
    for i in range(len(neighbors)):
        
        _, letter = neighbors[i]
        next_coordinates, _ = neighbors[(i+1) % len(neighbors)]
        
        letters[next_coordinates] = letter
        
    return letters
                
# Perform a single decoding, and track how each cell has moved
def get_next_steps(letters, instructions, max_x, max_y):
    cur_instruction = 0
    
    letter_positions = dict()
    
    for letter in letters:
        letter_positions[letter] = letter
    
    for y in range(1, max_y):
        for x in range(1, max_x):
            
            instruction = instructions[cur_instruction % len(instructions)]
            
            letters = do_rotation(instruction, letter_positions, (x,y))
            
            cur_instruction += 1

    return letters
    
# Identify cycles in the list of next steps
def get_cycles(next_steps):
    
    cycles = []
    
    while len(next_steps) > 0:
        
        key = list(next_steps.keys())[0]
        
        cycle = []
        
        while key in next_steps:
                        
            cycle.append(key)
            
            next_key = next_steps[key]
            
            del next_steps[key]

            key = next_key
            
        cycles.append(cycle)
        
    return cycles
        
# Find a given character in the grid
def find_character(letters, character):
    
    for letter in letters:
        if letters[letter] == character:
            return letter

# Given a location in the grid, find out where it end up after a number of 
# iterations, given the cycles
def get_location_after_iterations(location, cycles, iterations):
    
    # Find the cycle that it is part of
    loc_cycle = -1
    
    for cycle in cycles:
        if location in cycle:
            loc_cycle = cycle
            
    # Find its location in the cycle
    start_index = loc_cycle.index(location)
    
    # Return the locaiton in the cycle after the number of iterations
    return loc_cycle[(start_index - iterations) % len(loc_cycle)]

# Given a location, find out which character end up there after a number of 
# iterations
def get_character_after_iterations(location, cycles, iterations, letters):
    
    # Find the cycle that it is part of
    loc_cycle = -1
    
    for cycle in cycles:
        if location in cycle:
            loc_cycle = cycle
            
    # Find the index in the cycle
    start_index = loc_cycle.index(location)

    # Find the index in the cycle of the character that end up
    # at the place
    original_index = (start_index + iterations) % len(loc_cycle)
    
    return letters[loc_cycle[original_index]]

# Open and parse input
file = open('input_part3.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the notes
instructions, letters, max_y, max_x = parse(notes)

# Init the number of iterations
target_iterations = 1048576000

# Get the next steps
next_steps = get_next_steps(letters, instructions, max_x, max_y)            

# Turn the steps into cycles
cycles = get_cycles(next_steps)

# Find the start and end symbols in the original grid
start_location = find_character(letters, '>')
end_location = find_character(letters, '<')

# Find out where the start and end symbols end up after the given number of iterations
start_location_target = get_location_after_iterations(start_location, cycles, target_iterations)
end_location_target = get_location_after_iterations(end_location, cycles, target_iterations)

# Init empty keyword
keyword = ""

# For every space between the start and end, figure out what character ends up there
for i in range(start_location_target[0] + 1, end_location_target[0]):
    keyword += get_character_after_iterations((i, start_location_target[1]), cycles, target_iterations, letters)

# Print the result
print(f'The keyword is {keyword}')