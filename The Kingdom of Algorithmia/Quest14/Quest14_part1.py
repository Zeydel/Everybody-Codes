# Parse the input into list of steps
def parse(notes):
    
    return [step for step in notes.split(',')]

# Get the maximum height of the tree, given the steps
def get_max_height(steps):
    
    # Init max and current height
    cur_height = 0
    max_height = 0
    
    # For every step
    for step in steps:
        
        # Split into direction and length
        direction = step[0]
        length = int(step[1:])
        
        # We only care about steps that go up and down
        if direction not in ['U', 'D']:
            continue
        
        # If the direction is up, add length
        if direction == 'U':
            cur_height += length
        
        # Otherwise substract length
        if direction == 'D':
            cur_height -= length
            
        # If we have beat the current max, save it
        if cur_height > max_height:
            max_height = cur_height
            
    # Return the max
    return max_height
    
    
# Open and parse input
file = open('input_part1.txt','r')
notes = file.read()

# Parse the input
steps = parse(notes)

# Compute the max height
max_height = get_max_height(steps)

# Print the results
print(f'The height of the plant is {max_height}')