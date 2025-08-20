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
    
def get_keyword(letters, max_x, max_y):
    
    keyword = ""
    
    start_found = False
    
    for y in range(max_y+1):
        for x in range(max_x+1):
            
            if letters[(x, y)] == '<':
                return keyword
            
            if start_found:
                keyword += letters[(x, y)]
            
            if letters[(x, y)] == '>':
                start_found = True

# Open and parse input
file = open('input_part1.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the notes
instructions, letters, max_y, max_x = parse(notes)

cur_instruction = 0

# Go through the grid and rotate as specified
for y in range(1, max_y):
    for x in range(1, max_x):
        
        instruction = instructions[cur_instruction % len(instructions)]
        
        letters = do_rotation(instruction, letters, (x,y))
        
        cur_instruction += 1
        
# Print the result
print(f'The keyword is {get_keyword(letters, max_x, max_y)}')
